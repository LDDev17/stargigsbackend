from flask import Blueprint
from app.services.booking.controllers import (
 create_new_booking,
    get_booking,
    update_existing_booking,
    cancel_existing_booking,
    check_availability,
    search_bookings_controller
)

booking_blueprint = Blueprint('booking_bp', __name__)

booking_blueprint.route('/', methods=['POST'])(create_new_booking)  
booking_blueprint.route('/availability', methods=['GET'])(check_availability)  
booking_blueprint.route('/<int:id>', methods=['GET'])(get_booking)
booking_blueprint.route('/<int:id>', methods=['PUT'])(update_existing_booking)  
booking_blueprint.route('/<int:id>/cancel', methods=['DELETE'])(cancel_existing_booking)   
booking_blueprint.route('/search', methods=['GET'])(search_bookings_controller)
