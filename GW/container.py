from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("Container diagram for Product and Location Management System", direction="TB", graph_attr=graph_attr):
    customer = Person(
        name="Personal Customer", description="A customer of the X-Customer"
    )

    with SystemBoundary("Product and Location Management System"):
        webapp = Container(
            name="Web Application",
            technology="Java & Python",
            description="Delivers the static content and the single page application.",
        )

        spa = Container(
            name="Single-Page Application",
            technology="Javascript and Angular",
            description="Provides all of the system functionality to customers via their web browser.",
        )

        api = Container(
            name="API Application",
            technology="Python and Java",
            description="Provides functionality via a REST API.",
        )

        auth = Container(
            name="Authentication System", 
            technology="Google Identity Platform",
            description="Handles authentication and role-based access control."
        )

        notif = Container(
            name="Notification System",
            technology="Google Cloud Monitoring/ PubSub", 
            description="Sends notifications to the users.",
        )

        database = Database(
            name="Database",
            technology="Cloud SQL",
            description="Stores Product and Location information",
        )

        search = Container(
            name="Search",
            technology="Google Cloud Search",
            description="Complex search operations",
        )

        data_import_export = Container(
            name="Data Import/Export Tools",
            technology="Python Scripts",
            description="Upload and download data in various formats.",
        )

        recovery = Container(
            name="Backup and Disaster Recovery Systems",
            technology="Google Cloud Storage",
            description="Creates data backups and restores them in the event of a disaster.",
        )

        data_access = Container(
            name="Data Access Component",
            technology="Python and Java",
            description="Grants access requests, data viewing, data exporting, and ad hoc data access.",
        )

    erp = System(
        name="X-Customer ERP System",
        description="Existing ERP system to leverage and share vital operational data",
        external=True,
    )

    crm = System(
        name="X-Customer CRM System",
        description="Existing CRM system facilitate the flow of accurate and centralized customer-related data.",
        external=True,
    )

    customer >> Relationship("Visits x-customer.com/product using [HTTPS]") >> webapp
    customer >> Relationship("Views products and locations using") >> [spa]
    webapp >> Relationship("Delivers to the customer's web browser") >> spa
    spa >> Relationship("Make API calls to REST") >> api
    api >> Relationship("Reads from and writes to") >> database
    api >> Relationship("Handles users authentication and role-based access control") >> auth
    api >> Relationship("Sends notifications to the users") >> notif
    api >> Relationship("Imports/exports data") >> data_import_export
    api >> Relationship("Handles data backup and disaster recovery") >> recovery
    api >> Relationship("Manages data access") >> data_access
    api >> Relationship("Makes API calls to [JSON/HTTPS]") >> erp
    api >> Relationship("Makes API calls to [JSON/HTTPS]") >> crm
    customer << Relationship("Sends notifications to the users") << notif
    database << Relationship("Reads from") << search
    database << Relationship("Reads/Writes from") << data_import_export
    database << Relationship("Reads from") << recovery
