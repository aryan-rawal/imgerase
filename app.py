import streamlit as st
from rembg import remove
from PIL import Image

def remove_bg(image):
    # input_img = "img3.png"
    # output_img = "img.png"
    # inp = Image.open(image)
    output = remove(image , alpha_matting=True)
    # output.save(output_img)
    return output

def main():
    st.title("Background Remover")
    st.write("This is a simple web app to remove background from images. It uses the rembg library.")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg","png","jpeg"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)

    
    if st.button('Remove Background'):
        st.balloons()
        output = remove_bg(image)
        st.write("Right Click and Save Image on PC/ Long press and save image on mobile")
        st.image(output, caption='Output Image.', use_column_width=True)

    


    st.sidebar.title("About")
    st.sidebar.info(
        "This is a simple web app to remove background from images. It uses the rembg library."
    )
    st.sidebar.title("Github")
    st.sidebar.info(
        "This web app is maintained by [Aryan](htttps://github.com/aryan-rawal)"
    )
if __name__ == "__main__":
    main()
