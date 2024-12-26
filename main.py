# main.py
import Calls
import Coupons
import EMI
import FeedBack
import GlobalSearch
import Healings
import Home
import Leads.QR_Consnet
import Navigation
import Static.Address
import Task
import TopCustomersReport
import Users
from Admin.user import change_role_admin
from Leads import NewLead
from Leads.BulkFreeBooking import bulk_free_booking
from Leads.WhatsappIntegration import WhatsappIntegration
from Login import login_to_dashboard
from Static import Category
from Static.healer import add_new_healer


def main():
    # Log in once
    driver = login_to_dashboard()
    add_new_healer(driver)
    #bulk_free_booking(driver)
    #NewLead.new_lead(driver)
    #Leads.QR_Consnet.QR(driver)
    #WhatsappIntegration(driver)
    #Healings.healings(driver)
    #Home.home(driver)
    #Navigation.navigation(driver)
    #Task.tasks(driver)
    #Users.users(driver)
    #TopCustomersReport.top_Customers(driver)
    #Calls.calls(driver)
    #GlobalSearch.global_search(driver)
    #EMI.emi(driver)
    #FeedBack.feedback(driver)
    #Static.Address.address(driver)
    #Static.Category.category(driver)
    #Coupons.coupons(driver)
    driver.quit()


if __name__ == "__main__":
    main()

