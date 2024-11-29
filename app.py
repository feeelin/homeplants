from flask import Flask, render_template, request, redirect, url_for

from services.plants_classes_services import PlantsClassesServices
from services.plants_services import PlantServices

app = Flask(__name__)


@app.route('/')
def all_plants_page():
    plants = PlantServices().get_all()
    return render_template("index.html", plants=plants)


@app.route('/classes')
def all_classes_page():
    classes = PlantsClassesServices().get_all()
    return render_template("classes.html", classes=classes)


@app.route('/classes/edit/<int:id>', methods=['GET', 'POST'])
def edit_class_page(id: int):
    manager = PlantsClassesServices()
    if request.method == "POST":
        manager.update_by_id(id, request.form)
        return redirect(url_for("all_classes_page"))
    updating = manager.get_by_id(id)
    return render_template("update_class.html", updating=updating)


if __name__ == '__main__':
    app.run(debug=True)
