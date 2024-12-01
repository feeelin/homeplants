from flask import Flask, render_template, request, redirect, url_for
from jinja2 import StrictUndefined

from services.plants_classes_services import PlantsClassesServices
from services.plants_services import PlantServices
from services.plants_info_services import PlantsInfoService
from services.room_services import RoomServices
from services.places_services import PlacesServices

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def all_plants_page():
    plants = PlantServices().get_all()
    return render_template("plants/index.html", plants=plants)


@app.route('/plants/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant_page(id: int):
    manager = PlantServices()
    if request.method == "POST":
        manager.update_by_id(id, request.form)
        return redirect(url_for('all_plants_page'))
    plant = manager.get_by_id(id)
    return render_template("plants/update_plant.html", updating=plant)


@app.route('/plants/add', methods=['GET', 'POST'])
def add_plant_page():
    manager = PlantServices()
    plants_info_services = PlantsInfoService()

    if request.method == "POST":
        manager.create(request.form)
        return redirect(url_for('all_plants_page'))

    plants_info = plants_info_services.get_all()
    return render_template("plants/add_plant.html", plants_info=plants_info)


@app.route("/plants/delete/<int:id>")
def delete_plant_page(id: int):
    PlantServices().delete(id)
    return redirect(url_for('all_plants_page'))


@app.route('/plants_info/edit/<int:id>', methods=['GET', 'POST'])
def edit_plant_info_page(id: int):
    services = PlantsInfoService()

    if request.method == "POST":
        services.update_by_id(id, request.form)
        return redirect(url_for('all_plants_page'))

    classes = PlantsClassesServices().get_all()
    plant_info = services.get_by_id(id)
    return render_template("plants/update_plants_info.html", updating=plant_info, classes=classes)


@app.route('/plants_info/add', methods=['GET', 'POST'])
def add_plant_info_page():
    services = PlantsInfoService()
    if request.method == "POST":
        services.create(request.form)
        return redirect(url_for('all_plants_page'))
    classes = PlantsClassesServices().get_all()
    return render_template("plants/add_plant_info.html", classes=classes)


@app.route('/classes')
def all_classes_page():
    classes = PlantsClassesServices().get_all()
    return render_template("classes/classes.html", classes=classes)


@app.route('/classes/edit/<int:id>', methods=['GET', 'POST'])
def edit_class_page(id: int):
    manager = PlantsClassesServices()
    if request.method == "POST":
        manager.update_by_id(id, request.form)
        return redirect(url_for("all_classes_page"))
    updating = manager.get_by_id(id)
    is_deletable = manager.is_class_deletable(id)
    return render_template("classes/update_class.html", updating=updating, is_deletable=is_deletable)


@app.route("/classes/add", methods=["GET", "POST"])
def add_class_page():
    manager = PlantsClassesServices()
    if request.method == "POST":
        manager.create(request.form)
        return redirect(url_for('all_classes_page'))
    return render_template("classes/add_class.html")


@app.route("/classes/delete/<int:id>")
def delete_class_page(id: int):
    PlantsClassesServices().delete(id)
    return redirect(url_for('all_classes_page'))


@app.route("/rooms")
def all_rooms_page():
    rooms = RoomServices().get_all()
    return render_template("rooms/rooms.html", rooms=rooms)


@app.route("/rooms/edit/<int:id>", methods=['GET', 'POST'])
def edit_room_page(id: int):
    manager = RoomServices()
    if request.method == "POST":
        manager.update_by_id(id, request.form)
        return redirect(url_for("all_rooms_page"))
    updating = manager.get_by_id(id)
    return render_template("rooms/update_room.html", updating=updating)


@app.route("/rooms/add", methods=["GET", "POST"])
def add_room_page():
    manager = RoomServices()
    if request.method == "POST":
        manager.create(request.form)
        return redirect(url_for("all_rooms_page"))
    return render_template("rooms/add_room.html")


@app.route("/rooms/delete/<int:id>")
def delete_room_page(id: int):
    RoomServices().delete(id)
    return redirect(url_for('all_rooms_page'))


@app.route("/rooms/places/<int:room_id>", methods=['GET', 'POST'])
def room_places_page(room_id):
    room_manager = RoomServices()
    places_manager = PlacesServices()
    plants_manager = PlantServices()

    if request.method == "POST":
        places_manager.update_some_rows(request.form)
        redirect(f"/rooms/places/{room_id}")

    room = room_manager.get_by_id(room_id)
    places = places_manager.get_all_for_room(room_id)
    plants = plants_manager.get_all()
    return render_template("rooms/room_places.html", room=room, places=places, plants=plants)


if __name__ == '__main__':
    app.run(debug=True)
