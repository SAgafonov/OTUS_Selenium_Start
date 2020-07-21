import allure
import logging
from decimal import Decimal
from helpers.admin_helper import CSS_SELECTORS_FOR_PRODUCTS, CSS_SELECTORS_GENERAL

logger = logging.getLogger(__name__)
logger.setLevel('INFO')


@allure.epic("Authorized zone of admin panel")
@allure.feature("Authorization")
class TestAuthorization:

    @allure.title("Sign in")
    def test_login(self, admin_login_page):
        logger.info("<======== Run login test ========>")
        admin_login_page.login()
        if not admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["user_menu_selector"]).text == "John Doe":
            allure.attach(body=admin_login_page.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Incorrect username")
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["logout_btn_selector"])
        admin_login_page.logout()
        logger.info("========> End login test <========\n")

    @allure.title("Sign out")
    def test_logout(self, admin_login_page):
        logger.info("<======== Run logout test ========>")
        admin_login_page.login()
        admin_login_page.logout()
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_form_selector"])
        assert admin_login_page.look_for_element(selector=CSS_SELECTORS_GENERAL["login_selector"])
        logger.info("========> End logout test <========\n")


@allure.epic("Authorized zone of admin panel")
@allure.feature("Actions with Products")
class TestProducts:

    @allure.title("Check 'Products' page")
    def test_go_to_products(self, admin_product_page):
        logger.info("<======== Run navigation to 'Products' test ========>")
        admin_product_page.login()
        admin_product_page.admin_navigate_to_products()
        if not admin_product_page.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["table_of_products_title"]).text == "Product List":
            allure.attach(body=admin_product_page.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Incorrect name of 'Products' table")
        assert admin_product_page.look_for_element(selector=CSS_SELECTORS_FOR_PRODUCTS["table_of_products"])
        logger.info("========> End navigation to 'Products' test <========\n")

    @allure.title("Check editing of a product")
    def test_edit_product(self, admin_product_page, get_from_db):
        logger.info("<======== Run edit product test ========>")
        changed_fields, edited_prod_id = admin_product_page.edit_product()
        print(edited_prod_id, type(edited_prod_id))
        price_to_compare = "$" + "{:,.2f}".format(float(changed_fields["price_in_edit"]))
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")

        # check that data is changed in DB
        from_oc_product = get_from_db("SELECT model, quantity, price FROM oc_product "
                                      "WHERE product_id = {edited_prod_id};".format(edited_prod_id=edited_prod_id))[0]
        from_oc_product_description = get_from_db("SELECT name FROM oc_product_description "
                                                  "WHERE product_id = {edited_prod_id};".format(edited_prod_id=edited_prod_id))[0]
        assert from_oc_product == (changed_fields["model_in_edit"], int(changed_fields["quantity_in_edit"]), Decimal(changed_fields["price_in_edit"]))
        assert from_oc_product_description == (changed_fields["prod_name_in_edit"], )

        # check data on UI
        for row in rows_of_products_table:
            if changed_fields["prod_name_in_edit"] == row.find_element_by_css_selector("td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == changed_fields["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == changed_fields["quantity_in_edit"]
                return
        logger.info("========> End edit product test <========\n")

    def test_delete_product_after_insert(self, admin_product_page, get_from_db, insert_product_in_db):
        logger.info("<======== Run delete after SQL insert product test ========>")
        product_id = insert_product_in_db
        name_of_deleted_product, deleted_prod_id = admin_product_page.delete_product(name='TEST123_{id}'.format(id=product_id))
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")

        # check that data is deleted in DB
        from_oc_product = get_from_db("SELECT model, quantity, price FROM oc_product "
                                      "WHERE product_id = {id};".format(id=product_id))
        from_oc_product_description = get_from_db("SELECT name FROM oc_product_description "
                                                  "WHERE product_id = {id};".format(id=product_id))
        assert from_oc_product == []
        assert from_oc_product_description == []

        # check that data is deleted on UI
        for row in rows_of_products_table:
            assert name_of_deleted_product not in row.text
        logger.info("========> End delete after SQL insert product test <========\n")

    # For adding via UI
    @allure.title("Check deleting of a product")
    def test_delete_product(self, admin_product_page, get_from_db):
        logger.info("<======== Run delete product test ========>")
        name_of_deleted_product, deleted_prod_id = admin_product_page.delete_product()
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")

        # check that data is deleted in DB
        from_oc_product = get_from_db("SELECT model, quantity, price FROM oc_product "
                                      "WHERE product_id = {deleted_prod_id};".format(deleted_prod_id=deleted_prod_id))
        from_oc_product_description = get_from_db("SELECT name FROM oc_product_description "
                                                  "WHERE product_id = {deleted_prod_id};".format(deleted_prod_id=deleted_prod_id))
        assert from_oc_product == []
        assert from_oc_product_description == []

        # check that data is deleted on UI
        for row in rows_of_products_table:
            assert name_of_deleted_product not in row.text
        logger.info("========> End delete product test <========\n")

    @allure.title("Check adding of a product")
    def test_add_product(self, admin_product_page, get_from_db):
        logger.info("<======== Run add product test ========>")
        created_fields = admin_product_page.create_product()
        price_to_compare = "$" + "{:,.2f}".format(float(created_fields["price_in_edit"]))
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")

        # check that data is deleted in DB
        from_oc_product = get_from_db("SELECT model, quantity, price FROM oc_product "
                                      "WHERE model = '{model}';".format(model=created_fields["model_in_edit"]))[0]
        from_oc_product_description = get_from_db("SELECT name FROM oc_product_description "
                                                  "WHERE name = '{name}';".format(name=created_fields["prod_name_in_edit"]))[0]
        assert from_oc_product == (created_fields["model_in_edit"], int(created_fields["quantity_in_edit"]),
                                   Decimal(created_fields["price_in_edit"]))
        assert from_oc_product_description == (created_fields["prod_name_in_edit"],)

        # check that data is deleted on UI
        for row in rows_of_products_table:
            if created_fields["prod_name_in_edit"] == row.find_element_by_css_selector(
                    "td:nth-child(3)").text:
                assert row.find_element_by_css_selector("td:nth-child(4)").text == created_fields["model_in_edit"]
                assert row.find_element_by_css_selector("td:nth-child(5)").text == price_to_compare
                assert row.find_element_by_css_selector("td:nth-child(6)").text == created_fields["quantity_in_edit"]
                return
        logger.info("========> End add product test <========\n")

    @allure.title("Check copying of a product")
    def test_copy_product(self, admin_product_page):
        logger.info("<======== Run copy product test ========>")
        name_of_copied_product = admin_product_page.copy_product()
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")
        temp = 0
        for row in rows_of_products_table:
            logger.debug("Look for all products with '{}' name".format(name_of_copied_product))
            if row.find_element_by_css_selector("td:nth-child(3)").text == name_of_copied_product:
                temp += 1
        logger.debug("Delete a copy of '{}' product".format(name_of_copied_product))
        admin_product_page.delete_product(name_of_copied_product)
        assert temp == 2
        logger.info("========> End copy product test <========\n")

    @allure.title("Check if 'Filter' form exists")
    def test_filter_form_exists(self, admin_product_page):
        assert admin_product_page.driver.find_element_by_css_selector(CSS_SELECTORS_FOR_PRODUCTS["table_for_filtering"])

    @allure.title("Check filtering of products by name")
    def test_filter_by_name(self, admin_product_page):
        logger.info("<======== Run filter product by name test ========>")
        filtered_name = admin_product_page.filter_product("name")
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")
        assert len(rows_of_products_table) == 1
        if not rows_of_products_table[0].find_element_by_css_selector("td:nth-child(3)").text == filtered_name:
            allure.attach(body=admin_product_page.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Element '{}' is not appeared".format(filtered_name))
        admin_product_page.remove_filtration("name")
        logger.info("========> End filter product by name test <========\n")

    @allure.title("Check filtering of products by model")
    def test_filter_by_model(self, admin_product_page):
        logger.info("<======== Run filter product by model test ========>")
        filtered_name = admin_product_page.filter_product("model")
        rows_of_products_table = admin_product_page.look_for_elements(selector="tbody tr")
        assert len(rows_of_products_table) == 1
        if not rows_of_products_table[0].find_element_by_css_selector("td:nth-child(4)").text == filtered_name:
            allure.attach(body=admin_product_page.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Element '{}' is not appeared".format(filtered_name))
        admin_product_page.remove_filtration("model")
        logger.info("========> End filter product by model test <========\n")

    def test_delete_all(self, admin_product_page, get_from_db):
        logger.info("<======== Run delete all products test ========>")
        admin_product_page.delete_all_products()

        # check that data is deleted on UI
        if not admin_product_page.look_for_element(selector="tbody tr").text == "No results!":
            allure.attach(body=admin_product_page.driver.get_screenshot_as_png(),
                          attachment_type=allure.attachment_type.PNG)
            raise AssertionError("Incorrect test in empty table")

        # check that data is deleted in DB
        from_oc_product = get_from_db("SELECT model, quantity, price FROM oc_product;")
        from_oc_product_description = get_from_db("SELECT name FROM oc_product_description;")
        assert from_oc_product == []
        assert from_oc_product_description == []

        # admin_product_page.create_product()
        logger.info("========> End delete all products test <========\n")

    # def test_add_3_pictures_to_product(self, admin_product_page):
    #     admin_product_page.login()
    #     admin_product_page.admin_navigate_to_products()
    #     admin_product_page.upload_image()
