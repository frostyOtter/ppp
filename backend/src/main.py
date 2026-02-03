import base64
import os
import tempfile
import traceback
from pathlib import Path

import streamlit as st

# Replace built-in logging with loguru
from loguru import logger

# Import our parser modules
from parsers import (
    analyze_pdf_structure,
    get_available_parsers,
    get_parser,
    pdf_diagnostic_info,
)

# Set page config
st.set_page_config(
    page_title="PDF Parsers Playground", layout="wide", initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown(
    """
<style>
    .main-header {
        color: white;
        background-color: #2e7d32;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        text-align: center;
    }
    .upload-section, .examples-section, .preview-section {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        border: 1px solid #e0e0e0;
    }
    .settings-section {
        background-color: white;
        padding: 20px;
        border-radius: 5px;
        margin-bottom: 20px;
        border: 1px solid #e0e0e0;
    }
    .tab-content {
        padding: 20px;
        border: 1px solid #e0e0e0;
        border-radius: 0 0 5px 5px;
    }
    .convert-btn {
        background-color: #2e7d32;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        margin-right: 10px;
    }
    .clear-btn {
        background-color: #e0e0e0;
        color: black;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# App title
st.markdown(
    '<div class="main-header"><h1>PDF Parsers Playground</h1><p>Playground for quick and easy experiment with many popular open-source PDF parsers</p></div>',
    unsafe_allow_html=True,
)


# Function to load example PDFs from the data directory
def load_example_pdfs():
    data_dir = Path("data")
    if data_dir.exists() and data_dir.is_dir():
        return [f.name for f in data_dir.glob("*.pdf")]
    else:
        # If data directory doesn't exist, return sample filenames
        logger.warning("Data directory not found. Using sample filenames.")
        return [
            "academic_paper_figure.pdf",
            "attention_paper.pdf",
            "complex_layout.pdf",
            "handwriting_form.pdf",
            "invoice.pdf",
            "magazine_complex_layout.pdf",
            "table.pdf",
        ]


# Function to display PDF preview
def display_pdf_preview(pdf_file):
    if pdf_file:
        # Create a temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(pdf_file.getvalue())
            tmp_path = tmp.name

        # Read the PDF file
        try:
            with open(tmp_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode("utf-8")

            # Display PDF
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="500" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)

            # Clean up the temporary file
            os.unlink(tmp_path)
            return True
        except Exception as e:
            logger.error(f"Error displaying PDF: {e}")
            st.error(f"Error displaying PDF: {e}")
            # Clean up the temporary file
            os.unlink(tmp_path)
            return False
    return False


# Save uploaded PDF to a temporary file
def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.getvalue())
        logger.info(f"Saved uploaded file to {tmp.name}")
        return tmp.name


# Initialize session state
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "example_file" not in st.session_state:
    st.session_state.example_file = None
if "pdf_content" not in st.session_state:
    st.session_state.pdf_content = None
if "conversion_result" not in st.session_state:
    st.session_state.conversion_result = None
if "current_parser" not in st.session_state:
    st.session_state.current_parser = None
if "diagnostic_info" not in st.session_state:
    st.session_state.diagnostic_info = None

# Get available parsers
available_parsers = get_available_parsers()

# Create the layout with two columns
left_col, right_col = st.columns([1, 1])

# LEFT COLUMN
with left_col:
    # Upload Section
    st.markdown('<div class="upload-section">', unsafe_allow_html=True)
    st.subheader("Upload PDF document")
    uploaded_file = st.file_uploader(
        "Upload your PDF file", type="pdf", label_visibility="collapsed"
    )
    if uploaded_file is not None:
        logger.info(f"File uploaded: {uploaded_file.name}")
        st.session_state.uploaded_file = uploaded_file
        st.session_state.example_file = None  # Clear example selection when uploading
    st.markdown("</div>", unsafe_allow_html=True)

    # Examples Section
    st.markdown('<div class="examples-section">', unsafe_allow_html=True)
    st.subheader("Examples")
    example_files = load_example_pdfs()
    example_cols = st.columns(3)
    for i, example in enumerate(example_files):
        with example_cols[i % 3]:
            if st.button(example, key=f"example_{i}"):
                logger.info(f"Example selected: {example}")
                st.session_state.example_file = example
                st.session_state.uploaded_file = (
                    None  # Clear uploaded file when selecting example
                )
    st.markdown("</div>", unsafe_allow_html=True)

    # PDF Preview Section
    st.markdown('<div class="preview-section">', unsafe_allow_html=True)
    st.subheader("PDF preview")

    if st.session_state.uploaded_file:
        logger.info("Displaying uploaded PDF preview")
        display_pdf_preview(st.session_state.uploaded_file)
        # Save the file path for processing
        temp_file_path = save_uploaded_file(st.session_state.uploaded_file)
        st.session_state.pdf_content = temp_file_path

        # Generate diagnostic info for the file
        try:
            st.session_state.diagnostic_info = pdf_diagnostic_info(temp_file_path)
        except Exception as e:
            logger.error(f"Error generating diagnostic info: {e}")
            st.session_state.diagnostic_info = (
                f"# Error\n\nError generating diagnostic info: {str(e)}"
            )

    elif st.session_state.example_file:
        st.info(f"Example selected: {st.session_state.example_file}")
        # In a real app, you would load the example file from your data directory
        example_path = Path("data") / st.session_state.example_file
        if example_path.exists():
            logger.info(f"Loading example file: {example_path}")
            with open(example_path, "rb") as f:
                st.session_state.pdf_content = str(example_path)
                # Create a file-like object for preview display
                file_content = f.read()
                st.markdown(f"Preview of {st.session_state.example_file}:")
                pdf_base64 = base64.b64encode(file_content).decode("utf-8")
                pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="500" type="application/pdf"></iframe>'
                st.markdown(pdf_display, unsafe_allow_html=True)

            # Generate diagnostic info for the file
            try:
                st.session_state.diagnostic_info = pdf_diagnostic_info(
                    str(example_path)
                )
            except Exception as e:
                logger.error(f"Error generating diagnostic info: {e}")
                st.session_state.diagnostic_info = (
                    f"# Error\n\nError generating diagnostic info: {str(e)}"
                )
        else:
            logger.warning(f"Example file not found: {example_path}")
            st.warning(f"Example file not found: {example_path}")
            st.session_state.pdf_content = None
            st.session_state.diagnostic_info = None
    st.markdown("</div>", unsafe_allow_html=True)

# RIGHT COLUMN
with right_col:
    # Conversion Methods Section
    st.markdown('<div class="settings-section">', unsafe_allow_html=True)
    st.subheader("Conversion methods (select one)")

    parser_options = list(available_parsers.keys())
    # Fix: Add a proper label for the selectbox
    selected_parser = st.selectbox(
        "Select a PDF parser",
        parser_options,
        label_visibility="collapsed",  # Hide the label visually but keep it for accessibility
    )
    st.session_state.current_parser = selected_parser

    # Advanced Settings
    with st.expander("Advanced settings", expanded=True):
        start_page = st.number_input(
            "Starting page (only max 5 consecutive pages are processed)",
            min_value=1,
            max_value=100,
            value=1,
        )
        debug_viz = st.checkbox("Enable debug visualization", value=True)

    # Convert and Clear buttons
    cols = st.columns(2)
    with cols[0]:
        convert_clicked = st.button(
            "Convert", key="convert_btn", use_container_width=True
        )
    with cols[1]:
        clear_clicked = st.button("Clear", key="clear_btn", use_container_width=True)

    if clear_clicked:
        logger.info("Clearing application state")
        st.session_state.uploaded_file = None
        st.session_state.example_file = None
        st.session_state.pdf_content = None
        st.session_state.conversion_result = None
        st.session_state.diagnostic_info = None
        st.experimental_rerun()

    if convert_clicked and st.session_state.pdf_content:
        with st.spinner(f"Converting with {selected_parser}..."):
            try:
                logger.info(f"Starting conversion with {selected_parser}")
                # Get the selected parser
                parser = get_parser(selected_parser)

                # Verify the file exists
                if not os.path.exists(st.session_state.pdf_content):
                    st.error(f"File not found: {st.session_state.pdf_content}")
                    logger.error(f"File not found: {st.session_state.pdf_content}")
                else:
                    logger.info(
                        f"File exists and ready for processing: {st.session_state.pdf_content}"
                    )

                    # Call the parser's extract_text method
                    conversion_result = parser.extract_text(
                        st.session_state.pdf_content, start_page, 5
                    )
                    logger.info("Conversion completed successfully")
                    st.session_state.conversion_result = conversion_result
            except Exception as e:
                error_details = traceback.format_exc()
                logger.error(f"Conversion error: {str(e)}\n{error_details}")
                st.error(f"Conversion error: {str(e)}")
                # Store the error as the conversion result
                st.session_state.conversion_result = (
                    f"# Error\n\n```\n{error_details}\n```"
                )

    # Results tabs
    if st.session_state.conversion_result:
        tabs = st.tabs(
            [
                "Markdown render",
                "Markdown text",
                "Debug visualization",
                "About",
                "Diagnostics",
            ]
        )

        with tabs[0]:  # Markdown render
            st.markdown(st.session_state.conversion_result)

        with tabs[1]:  # Markdown text
            st.code(st.session_state.conversion_result, language="markdown")

        with tabs[2]:  # Debug visualization
            if debug_viz:
                if st.session_state.pdf_content and os.path.exists(
                    st.session_state.pdf_content
                ):
                    try:
                        # Get structured analysis of the PDF
                        pdf_analysis = analyze_pdf_structure(
                            st.session_state.pdf_content
                        )
                        st.markdown(pdf_analysis)
                    except Exception as e:
                        st.error(f"Error analyzing PDF structure: {str(e)}")
                else:
                    st.info("No PDF file available for debug visualization.")
            else:
                st.info("Debug visualization is disabled")

        with tabs[3]:  # About
            parser = get_parser(st.session_state.current_parser)
            st.markdown(f"## {parser.name}")
            st.markdown(parser.description)
            st.markdown(f"[Learn more]({parser.link})")

        with tabs[4]:  # Diagnostics
            if st.session_state.diagnostic_info:
                st.markdown(st.session_state.diagnostic_info)
            else:
                st.info("No diagnostic information available.")

    st.markdown("</div>", unsafe_allow_html=True)

# Clean up temporary files when the app is done
if (
    hasattr(st.session_state, "pdf_content")
    and st.session_state.pdf_content
    and os.path.exists(st.session_state.pdf_content)
):
    try:
        # Check if it's a temporary file (not an example file)
        if st.session_state.pdf_content.startswith(tempfile.gettempdir()):
            logger.info(f"Cleaning up temporary file: {st.session_state.pdf_content}")
            os.unlink(st.session_state.pdf_content)
    except Exception as e:
        logger.error(f"Error cleaning up temporary file: {e}")
