from diagrams import Cluster, Diagram, Edge
from diagrams.custom import Custom
from diagrams.onprem.client import Users
from diagrams.onprem.compute import Server
from diagrams.onprem.vcs import Github
from diagrams.gcp.devtools import GCR, Build
from diagrams.gcp.network import Armor
from diagrams.gcp.database import SQL
from diagrams.gcp.analytics import BigQuery
from diagrams.gcp.storage import GCS
from diagrams.gcp.compute import GKE
from diagrams.gcp.analytics import PubSub
from diagrams.gcp.security import Iam

with Diagram("Deployment diagram", show=False):
    users = Users("users")
    devs = Users("developers")
    vcs = Github("Version Control GitHub ")

    with Cluster("External Services"):
        with Cluster("X-Customer Integreations"):
            integrations = [
                Server("CRM integration"),
                Server("ERP integration")
            ]
        with Cluster("External Systems"):
            extenral_systems = [
                Server("Vendor Systems"),
                Server("Partener Systems")
            ]

    with Cluster("Google Cloud"):

        with Cluster("CI/CD"):
            artifacts= GCR("Artifact Registry")
            build= Build("Cloud Build")
        
        with Cluster("Database HA"):
            profile_db = SQL("Profile DB")
            product_db = SQL("Product DB")
            location_db = SQL("Location DB")
            
        with Cluster("API Management"):
            armor= Armor("Cloud Armor")
            armor \
                - Edge(style="dotted") \
                - Custom("Apigee", "./resources/apigee.png") \
                << Edge(label="collect")
        

        with Cluster("Frontend"):
            front_service = GKE("Front End Service")
            front_service \
            - Edge(style="dotted") \
            - GCS("frontend") \
            << Edge(label="static content")

        with Cluster("API"):
            with Cluster("Services"):
                auth_service = GKE("Auth Service")
                auth_service \
                - Edge(style="dotted") \
                - Iam("RBAC validations") \
                << Edge(label="collect")
                profile_service = GKE("Profile Service")
                product_service = GKE("Product Service")
                location_service = GKE("Location Service")
                notification_service = GKE("Notification Service")
                notification_service \
                - Edge(style="dotted") \
                - PubSub("notifications") \
                << Edge(label="collect")

        with Cluster("Analytics"):
            datawarehouse = BigQuery("Data Warehouse")
            datawarehouse \
            - Edge(style="dotted") \
            - Custom("Looker", "./resources/looker.png") \
            << Edge(label="collect")


    users >> armor >> auth_service
    devs >> vcs >> build
    notification_service >> users
    front_service >> auth_service >> [profile_service, product_service, location_service, notification_service]
    armor >> front_service >> auth_service
    profile_service >> profile_db
    product_service >> product_db
    location_service >> location_db
    [profile_db, product_db, location_db] >> datawarehouse
    datawarehouse >> users
    profile_service >> integrations
    product_service >> integrations
    location_service >> integrations
    profile_service >> extenral_systems
    product_service >> extenral_systems
    location_service >> extenral_systems