from models.subject_model import attendance_advice
from models.subject_model import get_today_subjects, calculate_percentage
from flask import Blueprint, render_template, request, redirect, url_for
from models.subject_model import (
    add_subject,
    get_all_subjects,
    get_subject,
    update_subject,
    delete_subject,
    mark_attendance,
    calculate_percentage
)

subject_bp = Blueprint("subject", __name__)

@subject_bp.route("/")
def home():
    subjects = get_today_subjects()

    for s in subjects:
        present = s["present"]
        absent = s["absent"]

        s["total"] = present + absent
        s["percentage"] = 0 if s["total"] == 0 else round((present/s["total"]) * 100)

    return render_template("home.html", subjects=subjects)


@subject_bp.route("/overall")
def dashboard():
    subjects = get_all_subjects()
    total_present = 0
    total_absent = 0

    for s in subjects:
        s["percentage"] = calculate_percentage(s["present"], s["absent"])

        total_present += s["present"]
        total_absent += s["absent"]

    total_classes = total_present + total_absent
    overall_percent = 0 if total_classes == 0 else round((total_present/total_classes)*100)
    advice = attendance_advice(total_present, total_absent, 75)

    summary = {
        "total_subjects": len(subjects),
        "total_classes": total_classes,
        "overall_percent": overall_percent,
        "status": advice["status"],
        "attend": advice["need_attend"],
        "bunk": advice["can_bunk"]   
    }
    return render_template("dashboard.html", subjects=subjects, summary=summary)


@subject_bp.route("/subjects")
def subjects():
    subjects = get_all_subjects()
    return render_template("manage_subjects.html", subjects=subjects)


@subject_bp.route("/all")
def all_subjects():
    subjects = get_all_subjects()

    for s in subjects:
        s["percentage"] = calculate_percentage(s["present"], s["absent"])

    return render_template("all_subjects.html", subjects=subjects)


@subject_bp.route("/subject/<int:id>")
def subject_detail(id):
    s = get_subject(id)

    total = s["present"] + s["absent"]
    percent = calculate_percentage(s["present"], s["absent"])

    return render_template(
        "subject_detail.html",
        subject=s,
        total=total,
        percent=percent
    )


@subject_bp.route("/add", methods=["GET", "POST"])
@subject_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":

        name = request.form["name"]
        days_list = request.form.getlist("days")
        days = ",".join(days_list)

        present = int(request.form["present"])
        absent = int(request.form["absent"])
        goal = request.form["goal"]

        add_subject(name, days, present, absent, goal)

        return redirect(url_for("subject.subjects"))

    return render_template("add_subject.html")


@subject_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    subject = get_subject(id)

    if request.method == "POST":
        name = request.form["name"]

        days_list = request.form.getlist("days")
        days = ",".join(days_list)

        present = int(request.form["present"])
        absent = int(request.form["absent"])
        goal = int(request.form["goal"])

        update_subject(id, name, days, present, absent, goal)

        return redirect(url_for("subject.subjects"))

    return render_template("edit_subject.html", subject=subject)


@subject_bp.route("/delete/<int:id>")
def delete(id):
    delete_subject(id)
    return redirect(url_for("subject.subjects"))


@subject_bp.route("/mark/<int:id>/<action>")
def mark(id, action):
    mark_attendance(id, action)
    return redirect(url_for("subject.home"))
