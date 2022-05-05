"""MM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import EmployeeView
from.import stateCityView
from.import Categoryview
from.import SubCategoryView
from.import ProductView
from.import Material
from.import finalProduct
from.import supplierView
from.import PurchaseView
from .import IssueView
from.import AdminView
from.import IssueView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AdminLogin/',AdminView.AdminView),
    path('checkadminlogin',AdminView.checkAdminLogin),
    path('employeeinterface/',EmployeeView.EmployeeInterface),
    path("employeesubmit", EmployeeView.EmployeeSubmit),
    path("DisplayAll/", EmployeeView.DisplayAll),
    path("DisplayEmployeeById/", EmployeeView.DisplayById),
    path('adminlogout',AdminView.AdminLogout),
    path('EmployeeDashboard',EmployeeView.EmployeeDashboard),
    path('AdminDashBoard/',AdminView.AdminView),

    path('fetchallstates/', stateCityView.FetchALLStates),
    path("fetchallcities/",stateCityView.FetchALLCities),
    path("category/",Categoryview.CategoryView),
    path("categorysubmit",Categoryview.CategorySubmit),
    path('SubCategory/',SubCategoryView.CategoryView),
    path('SubCategorySubmit',SubCategoryView.SubCategorySubmit),
    path('productview/',ProductView.pView),
    path("productsubmit",ProductView.ProductSubmit),
    path("DisplayAllCategory/", Categoryview.DisplayallCategory),
    path("EditDeleteEmployee",EmployeeView.EditDeleteRecord),
    path('EditEmployeePicture/',EmployeeView.EditEmployeePicture),
    path('SaveEditPicture',EmployeeView.SaveEditPicture),
    path('DisplayCategoryById/',Categoryview.DisplayById),
    path("EditDeleteCategory",Categoryview.EditDeleteCategory),
    path('SaveEditCategoryIcon',Categoryview.SaveEditCategoryIcon),
    path('EditCategoryIcon/',Categoryview.EditCategoryIcon),
    path('DisplaySubCategory/',SubCategoryView.DisplaySubCategories),
    path('DisplaySubCategoryById',SubCategoryView.DisplaySubcategoryById),
    path('EditDeleteSubCategory',SubCategoryView.EditDeleteSubategory),
    path('EditSubCategoryIcon/',SubCategoryView.EditSubategoryIcon),
    path('SaveEditSubCategoryIcon',SubCategoryView.SaveEditSubcategoryIcon),
    path('ProductDisplay/',ProductView.DisplayProducts),
    path('EditDeleteProduct',ProductView.EditDeleteProduct),
    path('EditProductById/',ProductView.DisplayById),
    path('EditProductIcon',ProductView.EditProductIcon),
    path('SaveEditProductIcon',ProductView.SaveEditProductIcon),

    path('MaterialView/',Material.MaterialInterface),
    path('FinalProductView/', finalProduct.ProdcutInterface),
    path('FinalProductSubmit',finalProduct.finalproductsubmit),
    path('getfinalproductjson',finalProduct.GetfinalProductJSON),
    path('getproductjson/',ProductView.GetProductJSON),
    path('getsubcategoryjson/',SubCategoryView.GetSubcategoryJSON),
    path('getcategoryjson/',Categoryview.GetCategoryJSON),
    path('getcategoriesjson',Categoryview.GetCategoryJSON),
    path('displayfinalproduct/',finalProduct.DisplayallProduct),
    path('supplierinterface',supplierView.supplierInterface),
    path('SupplierSubmit',supplierView.SupplierSubmit),
    path('supplierbyid/',supplierView.DisplayById),
    path('EditDeleteSupplier',supplierView.Displayallsupplier),
    path('DisplayAllSupplier/',supplierView.Displayallsupplier),
    path('getsupplierjson/', supplierView.GetsupplierJSON),
    path('purchaseinterface/',PurchaseView.PurchaseInterface),
    path('purchasesubmit',PurchaseView.PurchaseSubmit),
    path('displayallpurchase/',PurchaseView.DisplayAllPurchase),
    path('EditDeletePurchaseRecord/',PurchaseView.EditDeletePurchasetRecord),

    path('issueinterface/', IssueView.IssueInterface),
    path('issueproductsubmit', IssueView.IssueProductSubmit),
    path('displayallissueproduct/', IssueView.DisplayAllIssueProduct),
    path('editdeleteissueproductrecord/', IssueView.EditDeleteIssueProductRecord),

    path('employeelogin/', EmployeeView.EmployeeLogin),
    path('employeedashboard/', EmployeeView.EmployeeDashboard),
    path('checkemployeelogin', EmployeeView.CheckEmployeeLogin),
    path('employeelogout', EmployeeView.EmployeeLogout),

    path('displayfinalproductbyidjson/', finalProduct.DisplayFinalProductByIdJSON),
    path('displayfinalproductalljson/', finalProduct.DisplayFinalProductAllJSON),
    path('displayupdatedstock/', finalProduct.DisplayUpdatedStock),
    path('displayupdateddate',finalProduct.DisplayUpdatedStockdate),
]
