import streamlit as st
from sklearn.tree import DecisionTreeClassifier

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="AI Student Early Warning System",
    page_icon="🎓",
    layout="wide"
)

# =====================================================
# AI TRAINING DATA
# =====================================================

X = [
    [90, 85, 8, 82],
    [75, 65, 7, 70],
    [55, 42, 3, 48],
    [45, 35, 2, 40],
    [68, 50, 5, 55],
    [85, 78, 7, 80],
    [50, 38, 2, 42],
    [70, 60, 6, 65]
]

y = [
    "Low",
    "Low",
    "High",
    "High",
    "Medium",
    "Low",
    "High",
    "Medium"
]

# =====================================================
# CREATE AND TRAIN MODEL
# =====================================================

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)

# =====================================================
# STUDENT DATABASE
# =====================================================

students = {

    "Raju": {
        "register_number": "10234567",
        "department": "Computer Science and Engineering",
        "course_name": "B.Tech",
        "year": "2nd Year",
        "semester": "Semester 3"
    },

    "Arun": {
        "register_number": "10234568",
        "department": "Computer Science and Engineering",
        "course_name": "B.Tech",
        "year": "2nd Year",
        "semester": "Semester 3"
    },

    "Priya": {
        "register_number": "10234569",
        "department": "Computer Science and Engineering",
        "course_name": "B.Tech",
        "year": "2nd Year",
        "semester": "Semester 3"
    },

    "Kiran": {
        "register_number": "10234570",
        "department": "Computer Science and Engineering",
        "course_name": "B.Tech",
        "year": "2nd Year",
        "semester": "Semester 3"
    },

    "Anu": {
        "register_number": "10234571",
        "department": "Computer Science and Engineering",
        "course_name": "B.Tech",
        "year": "2nd Year",
        "semester": "Semester 3"
    }
}

# =====================================================
# SUBJECT DATABASE
# =====================================================

subjects = [

    {
        "name": "Operating Systems",
        "code": "CSE 401"
    },

    {
        "name": "Design Thinking",
        "code": "CSE309"
    },

    {
        "name": "Graphics",
        "code": "AML291"
    },

    {
        "name": "Python Programming",
        "code": "CSE210"
    }
]

# =====================================================
# SESSION STATE
# =====================================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "prediction_done" not in st.session_state:
    st.session_state.prediction_done = False

if "results" not in st.session_state:
    st.session_state.results = []

# =====================================================
# FACULTY LOGIN
# =====================================================

if not st.session_state.logged_in:

    st.title("🎓 AI Student Early Warning System")

    st.subheader("👨‍🏫 Faculty Login")

    username = st.text_input(
        "Faculty Username"
    )

    password = st.text_input(
        "Faculty Password",
        type="password"
    )

    login_button = st.button(
        "🔐 Login",
        use_container_width=True
    )

    if login_button:

        if username == "faculty" and password == "1234":

            st.session_state.logged_in = True
            st.session_state.prediction_done = False

            st.rerun()

        else:

            st.error(
                "❌ Invalid Username or Password"
            )

    # Stop dashboard from appearing before login
    st.stop()


# =====================================================
# FACULTY DASHBOARD
# =====================================================

st.title("👨‍🏫 Faculty Dashboard")

st.write(
    "AI-powered Subject-wise Student Early Warning System"
)

# =====================================================
# LOGOUT
# =====================================================

if st.button("🚪 Logout"):

    st.session_state.logged_in = False
    st.session_state.prediction_done = False
    st.session_state.results = []

    st.rerun()

st.divider()

# =====================================================
# CLASS DASHBOARD
# =====================================================

st.header("📊 Class Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "👨‍🎓 Total Students",
        len(students)
    )

with col2:

    st.metric(
        "📚 Total Subjects",
        len(subjects)
    )

with col3:

    st.metric(
        "🤖 ML Model",
        "Decision Tree"
    )

with col4:

    st.metric(
        "⚡ System Status",
        "Active"
    )

st.divider()

# =====================================================
# STUDENT SELECTION
# =====================================================

st.header("👨‍🎓 Student Selection")

selected_student = st.selectbox(
    "Select Student",
    list(students.keys())
)

student = students[selected_student]

# =====================================================
# STUDENT DETAILS
# =====================================================

st.subheader("📋 Student Details")

col1, col2, col3 = st.columns(3)

with col1:

    st.write("**Student Name**")

    st.info(
        selected_student
    )

with col2:

    st.write("**Register Number**")

    st.info(
        student["register_number"]
    )

with col3:

    st.write("**Department**")

    st.info(
        student["department"]
    )


# Course Name and Year/Semester
col1, col2 = st.columns(2)

with col1:

    st.write("**Course Name**")

    st.info(
        student["course_name"]
    )

with col2:

    st.write("**Year / Semester**")

    st.info(
        f"{student['year']} / {student['semester']}"
    )

st.divider()

# =====================================================
# SUBJECT-WISE ACADEMIC DETAILS
# =====================================================

st.header("📚 Subject-wise Academic Details")

st.caption(
    "Faculty can enter the academic details for each subject."
)

subject_data = []

for i, subject in enumerate(subjects):

    st.subheader(
        f"📘 {subject['name']} — {subject['code']}"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0,
            max_value=100,
            value=75,
            step=1,
            key=f"{selected_student}_attendance_{i}"
        )

    with col2:

        internal_marks = st.number_input(
            "Internal Marks",
            min_value=0,
            max_value=100,
            value=60,
            step=1,
            key=f"{selected_student}_internal_{i}"
        )

    with col3:

        assignments = st.number_input(
            "Assignments Completed",
            min_value=0,
            max_value=10,
            value=6,
            step=1,
            key=f"{selected_student}_assignment_{i}"
        )

    with col4:

        previous_score = st.number_input(
            "Previous Exam Score",
            min_value=0,
            max_value=100,
            value=65,
            step=1,
            key=f"{selected_student}_previous_{i}"
        )

    subject_data.append({

        "name": subject["name"],
        "code": subject["code"],
        "attendance": attendance,
        "internal": internal_marks,
        "assignments": assignments,
        "previous": previous_score
    })

    st.divider()

# =====================================================
# AI PREDICTION
# =====================================================

if st.button(
    "🤖 Predict Student Risk",
    use_container_width=True
):

    results = []

    for subject in subject_data:

        input_data = [[
            subject["attendance"],
            subject["internal"],
            subject["assignments"],
            subject["previous"]
        ]]

        prediction = model.predict(
            input_data
        )[0]

        results.append(prediction)

    st.session_state.results = results
    st.session_state.prediction_done = True


# =====================================================
# PREDICTION RESULTS
# =====================================================

if st.session_state.prediction_done:

    results = st.session_state.results

    st.header("📊 Subject-wise AI Prediction")

    # =================================================
    # RISK COUNT
    # =================================================

    high_count = results.count("High")
    medium_count = results.count("Medium")
    low_count = results.count("Low")

    # =================================================
    # SUBJECT RESULTS
    # =================================================

    for i, subject in enumerate(subject_data):

        prediction = results[i]

        st.subheader(
            f"📘 {subject['name']} — {subject['code']}"
        )

        if prediction == "High":

            st.error(
                "🔴 HIGH RISK"
            )

            st.warning(
                "Immediate academic support is recommended."
            )

        elif prediction == "Medium":

            st.warning(
                "🟡 MEDIUM RISK"
            )

            st.info(
                "Regular monitoring is recommended."
            )

        else:

            st.success(
                "🟢 LOW RISK"
            )

            st.info(
                "Student performance is currently stable."
            )

        # Academic values
        col1, col2, col3, col4 = st.columns(4)

        with col1:

            st.metric(
                "Attendance",
                f"{subject['attendance']}%"
            )

        with col2:

            st.metric(
                "Internal Marks",
                subject["internal"]
            )

        with col3:

            st.metric(
                "Assignments",
                f"{subject['assignments']}/10"
            )

        with col4:

            st.metric(
                "Previous Score",
                subject["previous"]
            )

        st.divider()

    # =================================================
    # RISK SUMMARY
    # =================================================

    st.header("📈 Risk Summary")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🔴 High Risk",
            high_count
        )

    with col2:

        st.metric(
            "🟡 Medium Risk",
            medium_count
        )

    with col3:

        st.metric(
            "🟢 Low Risk",
            low_count
        )

    st.divider()

    # =================================================
    # OVERALL RISK
    # =================================================

    st.header("🎯 Overall Student Risk")

    if high_count >= 2:

        overall_risk = "High"

    elif high_count == 1 or medium_count >= 2:

        overall_risk = "Medium"

    else:

        overall_risk = "Low"

    if overall_risk == "High":

        st.error(
            "🔴 OVERALL RISK: HIGH"
        )

    elif overall_risk == "Medium":

        st.warning(
            "🟡 OVERALL RISK: MEDIUM"
        )

    else:

        st.success(
            "🟢 OVERALL RISK: LOW"
        )

    # =================================================
    # EARLY WARNING
    # =================================================

    st.header("⚠️ Early Warning Status")

    if overall_risk == "High":

        st.error(
            "🚨 EARLY WARNING GENERATED\n\n"
            "High academic risk detected. "
            "Immediate faculty intervention is recommended."
        )

    elif overall_risk == "Medium":

        st.warning(
            "⚠️ MONITORING ALERT\n\n"
            "Potential academic risk detected. "
            "Regular monitoring is recommended."
        )

    else:

        st.success(
            "✅ NO EARLY WARNING\n\n"
            "Student performance is currently stable."
        )

    # =================================================
    # FACULTY RECOMMENDATION
    # =================================================

    st.header("👨‍🏫 Recommended Faculty Action")

    if overall_risk == "High":

        st.write(
            "🔴 Provide immediate academic support."
        )

        st.write(
            "📌 Monitor attendance regularly."
        )

        st.write(
            "📚 Provide additional learning resources."
        )

        st.write(
            "👨‍🏫 Schedule regular faculty follow-up."
        )

    elif overall_risk == "Medium":

        st.write(
            "🟡 Monitor academic performance regularly."
        )

        st.write(
            "📌 Encourage better attendance."
        )

        st.write(
            "📚 Provide additional academic guidance."
        )

    else:

        st.write(
            "🟢 Continue regular academic monitoring."
        )

        st.write(
            "📚 Encourage consistent performance."
        )