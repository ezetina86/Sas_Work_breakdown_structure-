from diagrams import Diagram
from diagrams.c4 import Person, System, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("System Context diagram for Product and Location Management System", direction="TB", graph_attr=graph_attr):
    customer = Person(
        name="Personal Customer", description="A customer of the X-Customer"
    )

    main = System(
        name="Product and Location System",
        description="Allows customers to manage products and locations.",
        external=False,
    )

    erp = System(
        name="CompanyX ERP System",
        description="Existing ERP system to leverage and share vital operational data",
        external=True,
    )

    crm = System(
        name="CompanyX CRM System",
        description="Existing CRM system facilitate the flow of accurate and centralized customer-related data.",
        external=True,
    )


    external_vendor = System(
        name="External Vendor / Partner Systems",
        description="Vendor and partner systems to securely exchange GIN, LN and related data in real-time.",
        external=True,
    )


    customer >> Relationship("Manages products and locations") << main
    main >> Relationship("Makes API calls to [JSON/HTTPS]") >> erp
    main >> Relationship("Makes API calls to [JSON/HTTPS]") >> crm
    main >> Relationship("Exchanges data with [APIs]") >> external_vendor