import streamlit as st
import pandas as pd

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="TJ Photographer | Research & Portfolio",
    page_icon="📸",
    layout="wide"
)

# ================= SIDEBAR =================
st.sidebar.title("📌 Navigation")
section = st.sidebar.radio(
    "Go to:",
    [
        "Home",
        "About Me",
        "Research Focus",
        "Portfolio",
        "Services",
        "Analytics",
        "Tools & Skills",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.caption("TJ_Photographer © 2026")

# ================= HOME =================
if section == "Home":
    st.title("📸 TJ Photographer")
    st.subheader("Photography Research, Portfolio & Professional Practice")

    st.markdown(
        """
        Welcome to my Streamlit-based professional profile.  
        This page showcases my **research-driven photography practice**,  
        **creative portfolio**, and **data-informed decision making**.
        """
    )

# ================= ABOUT =================
elif section == "About Me":
    st.header("👤 About the Researcher & Photographer")

    st.write(
        """
        I am a student photographer based in Limpopo, operating under the brand
        **TJ_Photographer**. My work focuses on portrait, event, and lifestyle photography.

        My practice integrates **creative storytelling**, **technical expertise**,
        and **research methods** to improve both artistic quality and business growth.
        """
    )

# ================= RESEARCH =================
elif section == "Research Focus":
    st.header("🔬 Research Focus Areas")

    st.markdown(
        """
        - 📊 **Client Behaviour Analysis** – understanding client preferences  
        - 🎨 **Visual Composition Research** – lighting, colour, and framing  
        - 📈 **Social Media Performance Analysis** – engagement and reach  
        - 🧠 **User Experience Research** – booking and service improvement  
        """
    )

# ================= PORTFOLIO =================
elif section == "Portfolio":
    st.header("🖼️ Portfolio Showcase")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(
            "images/Portrait(Mogano Jtack Tshoane).jpg",
            caption="Portrait Photography",
            use_column_width=True
        )

    with col2:
        st.image(
            "images/Events(Mogano Jtack Tshoane).jpg",
            caption="Event Photography",
            use_column_width=True
        )

    with col3:
        st.image(
            "images/LifeStyle(Mogano Jtack Tshoane).jpg",
            caption="Lifestyle Photography",
            use_column_width=True
        )

# ================= SERVICES =================
elif section == "Services":
    st.header("📷 Photography Services")

    st.markdown(
        """
        **🎓 Graduation Shoots**  
        Professional graduation portraits (studio & outdoor).

        **🎂 Events & Birthdays**  
        Kids, adult birthdays, and baby showers.

        **🧑‍💼 Headshots**  
        Professional headshots for students and professionals.
        """
    )

# ================= ANALYTICS =================
elif section == "Analytics":
    st.header("📊 Research & Business Analytics")

    st.write(
        """
        The chart below demonstrates how booking data is analysed
        to identify high-demand photography services.
        """
    )

    data = pd.DataFrame({
        "Service": ["Graduation", "Birthdays", "Headshots", "Events"],
        "Bookings": [35, 25, 20, 15]
    })

    st.bar_chart(data.set_index("Service"))

# ================= TOOLS & SKILLS =================
elif section == "Tools & Skills":
    st.header("🛠️ Tools & Skills")

    st.markdown(
        """
        **Photography Tools**
        - DSLR / Mirrorless Cameras  
        - Speedlights & Studio Lighting  
        - Adobe Photoshop & Lightroom  

        **Research & Technical Skills**
        - Image retouching & colour grading  
        - Client data analysis  
        - Content performance evaluation  
        """
    )

# ================= CONTACT =================
elif section == "Contact":
    st.header("📬 Contact Information")

    st.markdown(
        """
        - 📧 Email: **tjphotographer@email.com**  
        - 📷 Instagram: **@tj_photographer**  
        - 📘 Facebook: **TJ Photographer**
        - 📘  WhatsApp: **072 912 3935**
        """
    )

    st.caption("© 2026 TJ_Photographer | Research-Informed Photography Practice")










