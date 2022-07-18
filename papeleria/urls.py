from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_admin", views.add_admin, name="add-admin"),
    path("add_admin_view", views.add_admin_view, name="add-admin-view"),
    path("add_customer", views.add_customer, name="add-customer"),
    path("add_customer_view", views.add_customer_view, name="add-customer-view"),
    path("add_product", views.add_product, name="add-product"),
    path("add_product_view", views.add_product_view, name="add-product-view"),
    path("add_seller", views.add_seller, name="add-seller"),
    path("add_seller_view", views.add_seller_view, name="add-seller-view"),
    path("edit_product/<int:reference>", views.edit_product, name="edit-product"),
    path("edit_product_view/<int:reference>", views.edit_product_view, name="edit-product-view"),
    path("delete_admin/<int:id>", views.delete_admin, name="delete-admin"),
    path("delete_customer/<int:id>", views.delete_customer, name="delete-customer"),
    path("delete_product/<int:reference>", views.delete_product, name="delete-product"),
    path("delete_seller/<int:id>", views.delete_seller, name="delete-seller"),
    path("list_admins", views.list_admins, name="list-admins"),
    path("list_customers", views.list_customers, name="list-customers"),
    path("list_products", views.list_products, name="list-products"),
    path("list_sellers", views.list_sellers, name="list-sellers"),
    path("login", views.login_view, name="login"),
    path("log-out", views.logout_view, name="log-out"),
    path("maintenance", views.maintenance, name="maintenance"),
    path("register", views.register, name="register"),
]