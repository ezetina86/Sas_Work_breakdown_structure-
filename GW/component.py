from diagrams import Diagram
from diagrams.c4 import System, SystemBoundary, Relationship, Database

graph_attr = {
    "splines": "spline",
}

with Diagram("API Application Component Diagram", direction="TB", graph_attr=graph_attr):

    with SystemBoundary("API Application"):
        profile_controller = System("Profile Controller", description="Manages profile related requests")
        product_controller = System("Product Controller", description="Handles product related requests")
        location_controller = System("Location Controller", description="Looks after location related requests")
        auth_controller = System("Authentication Controller", description="Responsible for authentication and authorization")
        notif_controller = System("Notification Controller", description="Sends notifications to users")

        profile_service = System("Profile Service", description="Processes profile related operations")
        product_service = System("Product Service", description="Processes product related operations")
        location_service = System("Location Service", description="Processes location related operations")
        auth_service = System("Authentication Service", description="Manages user authentication and access control")
        notif_service = System("Notification Service", description="Manages notifications sent to users")

        profile_repository = System("Profile Repository", description="Handles profile data persistence")
        product_repository = System("Product Repository", description="Handles product data persistence")
        location_repository = System("Location Repository", description="Handles location data persistence")

        profile_controller >> profile_service >> profile_repository
        product_controller >> product_service >> product_repository
        location_controller >> location_service >> location_repository

        auth_controller >> auth_service
        notif_controller >> notif_service

    spa = System("Single-Page Application", description="Interacts with the API application to serve user requests")
    spa >> Relationship("Makes API calls") >> profile_controller
    spa >> Relationship("Makes API calls") >> product_controller
    spa >> Relationship("Makes API calls") >> location_controller
    spa >> Relationship("Makes API calls") >> auth_controller
    spa >> Relationship("Receives notifications") << notif_controller

    profile_db = Database("Profile Database", description="Stores and retrieves profile data")
    product_db = Database("Product Database", description="Stores and retrieves product data")
    location_db = Database("Location Database", description="Stores and retrieves location data")
    
    profile_repository >> Relationship("Reads from and writes to") >> profile_db
    product_repository >> Relationship("Reads from and writes to") >> product_db
    location_repository >> Relationship("Reads from and writes to") >> location_db