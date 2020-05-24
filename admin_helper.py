USERNAME = "user"
PASSWORD = "bitnami1"

SELECTORS_GENERAL = {
    "login_form_selector": "div.panel-body form",
    "login_selector": "[name='username']",
    "password_selector": "[name='password']",
    "user_menu_selector": ".dropdown > .dropdown-toggle",
    "login_btn_selector": ".btn.btn-primary",
    "logout_btn_selector": "ul.nav.navbar-nav.navbar-right > li:nth-child(2)"
}
SELECTORS_LEFT_NAV_MENU = {
    "catalog_element": "#menu > #menu-catalog",
    "product_element": "li#menu-catalog > ul#collapse1 li:nth-child(2)"
}
SELECTORS_FOR_PRODUCTS = {
    "table_of_products_title": "div.col-md-9.col-md-pull-3.col-sm-12 h3",
    "table_of_products": "div.col-md-9.col-md-pull-3.col-sm-12 div.table-responsive table",
    "checkbox_select_all": "input[onclick]",
    "table_for_filtering": ".row .panel.panel-default .panel-body",
    "add_product_btn": ".btn.btn-primary[data-original-title='Add New']",
    "copy_product_btn": ".btn.btn-default[data-original-title='Copy']",
    "delete_product_btn": ".btn.btn-danger[data-original-title='Delete']",
    "edit_btn": ".table.table-bordered.table-hover tbody tr:first-child td.text-right:last-child > a",
    "filter_btn": "#button-filter",
    "filter_input_product_name": "#input-name",
    "filter_input_product_model": "#input-model",
    "tab_data_in_edit": "a[href='#tab-data']",
    "tab_special_in_edit": "a[href='#tab-special']",
    "tab_image_in_edit": "a[href='#tab-image']",
    "save_btn": "button[data-original-title='Save']",
    "prod_img": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(2)",
    "prod_name": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(3)",
    "prod_model": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(4)",
    "prod_price": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(5) > span",
    "prod_special_price": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(5) > div",
    "prod_quantity": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(6)",
    "prod_status": ".table.table-bordered.table-hover tbody tr:first-child td:nth-child(7)",
    "prod_name_in_edit": "input[name='product_description[1][name]']",
    "meta_tag_in_edit": "#input-meta-title1",
    "model_in_edit": "input#input-model",
    "status_in_edit": "#input-status",
    "price_in_edit": "input#input-price",
    "quantity_in_edit": "input#input-quantity",
    "special_price_in_edit": "input[name='product_special[0][price]']",
    "image_in_edit": "td.text-left > a#thumb-image > img"
}
