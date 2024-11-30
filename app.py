from flask import Flask, render_template, request, redirect, url_for

from services.plants_classes_services import PlantsClassesServices
from services.plants_services import PlantServices
from services.plants_info_services import PlantsInfoService

app = Flask(__name__)


@app.route('/')
def all_plants_page():
    plants = PlantServices().get_all()
    return render_template("index.html", plants=plants)


@app.route('/plants/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant_page(id: int):
    services = PlantServices()
    if request.method == "POST":
        services.update_by_id(id, request.form)
        return redirect(url_for('all_plants_page'))
    plant = services.get_by_id(id)
    return render_template("update_plant.html", updating=plant)


@app.route('/plants_info/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant_info_page(id: int):
    services = PlantsInfoService()

    if request.method == "POST":
        services.update_by_id(id, request.form)
        return redirect(url_for('all_plants_page'))

    classes = PlantsClassesServices().get_all()
    plant_info = services.get_by_id(id)
    return render_template("update_plants_info.html", updating=plant_info, classes=classes)


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
