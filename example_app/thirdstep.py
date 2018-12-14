import uuid
import json
import  datetime









def threesend(request):
    """k={"CorrelationID": request.POST["correlation_id"],
            "BusinessType": request.POST["business_type"],
            "DealId": request.POST["deal_id"],
            "VehicleMakeCode": request.POST["vehical_make_code"],
            "VehicleModelCode": request.POST["vehical_model_code"],
            "VehicleDescription": request.POST["vehical_description"],
            "RTOLocationCode": request.POST["rto_location_code"],
            "ExShowRoomPrice": request.POST["ex_showroom_price"],
            "IsNoPrevInsurance": request.POST["is_no_prev_insurance"],
            "Tenure": request.POST["tenure"],
            "ManufacturingYear": request.POST["manufacturing_year"],
            "DeliveryOrRegistrationDate": request.POST["delivery_or_registration_date"],
            "FirstRegistrationDate": request.POST["first_registration_date"],
            "IsTransferOfNCB": request.POST["is_transfer_of_ncb"],
            "TransferOfNCBPercent": float(request.POST["transfer_of_ncb_percent"]),
            "BonusOnPreviousPolicy": request.POST["bonus_on_previous_policy"],
            "PreviousPolicyStartDate": request.POST["previous_policy_start_date"],
            "PreviousPolicyEndDate": request.POST["previous_policy_end_date"],
            "PreviousPolicynumber": request.POST["previous_policy_number"],
            "ClaimOnPreviousPolicy": request.POST["claim_on_previous_policy"],
            "TotalNoOfODIClaims": request.POST["total_no_of_od_claims"],
            "PreviouslyPolicyType": request.POST["previous_policy_type"],
            "PreviousInsuranceName": request.POST["previous_insurance_name"],
            "PreviousPolicyNumber": request.POST["previous_policy_number"],
            #"PreviousPolicySaleDate": request.POST["previous_policy_sale_date"],
            "PreviousVehicleSaleDate": request.POST["previous_policy_tenure"],
            "PreviousPolicyTenure": request.POST["previous_policy_tenure"],
            "PolicyStartDate": request.POST["policy_start_date"],
            "PolicyEndDate": request.POST["policy_end_date"],
            "CustomerType": request.POST["customer_type"],
            "IsHaveElectricalAccessories": request.POST["is_have_electrical_accessories"],
            "SIHaveElectricalAccessories": request.POST["si_have_electrical_accessories"],
            "IsHaveNonElectricalAccessories": request.POST["is_have_non_electrical_accessories"],
            "SIHaveNonElectricalAccessories": request.POST["si_have_non_electrical_accessories"],
            "TPPDLimit": request.POST["tppd_limit"],
            "IsLegalLiabilityToPaidDriver": request.POST["is_legal_liability_to_paid_driver"],
            "IsLegalLiabilityToPaidEmpolyee": request.POST["is_legal_liability_to_paid_empolyee"],
            "NoOfEmpolyee": request.POST["no_of_empolyee"],
            "IsPACoverUnnamedPassenger": request.POST["is_pa_cover_unnamed_passenger"],
            "SIPACoverUnnamedPassenger": request.POST["sipa_cover_unnamed_passenger"],
            "IsValidDrivingLicense": request.POST["is_valid_driving_licence"],
            "IsMoreThanOneVehicle": request.POST["is_more_than_one_vehical"],
            "IsPACoverOwnerDriver": request.POST["is_pa_cover_owner_driver"],
            "IsVoluntaryDeductible": request.POST["is_voluntary_deductible"],
            "VoluntaryDeductiblePlanName": request.POST["voluntry_deductible_plan_name"],
            "IsAutomobileAssocnFlag": request.POST["is_automobile_assocn_flag"],
            "AutomobileAssociationNumber": request.POST["automobile_association_number"],
            "IsAntiTheftDisc": request.POST["is_anti_theft_disk"],
            "IsHandicapDisc": request.POST["is_handicap_disk"],
            "IsExtensionCountry": request.POST["is_extension_country"],
            "ExtensionCountryName":request.POST["extension_country_name"],
            "ZeroDepPlanName": request.POST["zero_dep_plan_name"],
            "IsRTIApplicableFlag": request.POST["is_rti_applicable_flag"],
            #"IsConsumables": request.POST["is_consumables"],
            #"IsEngineProtectPlus": request.POST["is_engine_protect_plus"],
            "RSAPlanName": request.POST["rsa_plan_name"],
            "OtherLoading": float(request.POST["other_loading"]),
            "OtherDiscount": float(request.POST["other_discount"]),
            "EngineNumber": request.POST["engine_number"],
            "ChassisNumber": request.POST["chassis_number"],
            "RegistrationNumber": request.POST["registration_number"],
            "NameOfNominee": request.POST["name_of_nominee"],
            "Age": request.POST["age"],
            "NomineeType": request.POST["nominee_type"],
            "Relationship": request.POST["relationship"],
            "CustomerTypes": request.POST["customer_type"],
            "CustomerName": request.POST["customer_name"],
            "DateOfBirth": request.POST["date_of_birth"],
            "PinCode": request.POST["pin_code"],
            "PANCardNumber": request.POST["pan_card_number"],
            "Email": request.POST["email"],
            "MobileNumber": request.POST["mobile_number"],
            "AddressLine1": request.POST["address_line_1"],
            "CountryCode": request.POST["country_code"],
            "StateCode": request.POST["state_code"],
            "CityCode": request.POST["city_code"],
            "Gender": request.POST["gender"],
            "MobileISD": request.POST["mobile_isd"],
            "GSTExemptionApplicable": request.POST["gst_exemption_applicable"],
            "GSTInNumber": request.POST["gst_in_number"],
            "GSTToState": request.POST["gstto_state"],
            "ConstituationOfBusiness": request.POST["constituation_of_business"],
            "CustomerType": request.POST["gcustomer_type"],
            "PanDetail": request.POST["pan_detail"],
            "GSTRegistrationStatus": request.POST["gst_registration_status"],
            "FinancierName": request.POST["financier_name"],
            "BrandName": request.POST["brand_name"],
            "AgreementType": request.POST["agreement_type"],

            }"""
    try:
        POST = json.loads(request.GET.get("data"))
    except:
        POST = request.GET
    k = {
            "BusinessType": "Roll Over",
            "DealId": "DL-3005/1483341",
            "VehicleMakeCode": str(int(31)),
            "VehicleModelCode":str(int(POST["VehicleModelCode"])),
        "DeliveryOrRegistrationDate": POST["reg_date"],
        "FirstRegistrationDate": POST["reg_date"],

        "PolicyStartDate": POST["new_date"],
        "PolicyEndDate": POST["new_date"],

        "ManufacturingYear": '',
        "Tenure": "1",
            "ExShowRoomPrice": str(int(float( POST["ExShowRoomPrice"]))),
"GSTToState":"MAHARASHTRA",
"CustomerType" : POST["CustomerType"],
            "RTOLocationCode": POST["RTOLocationCode"],
            "IsNoPrevInsurance": "false",
                        "CorrelationId":str(uuid.uuid4()),


"IsPACoverOwnerDriver":"TRUE",
            "IsPACoverUnnamedPassenger": "FALSE",


"RegistrationNumber": POST["RegistrationNumber"],
"EngineNumber": POST["EngineNumber"],
"ChassisNumber": POST["ChassisNumber"],
"VehicleDescription": POST["VehicleDescription"],




"DealId":"DL-3005/1483341",
        "DeliveryOrRegistrationDate": POST["reg_date"],
        "FirstRegistrationDate": POST["reg_date"],

        "PolicyStartDate": POST["new_date"],
        "PolicyEndDate": POST["new_date"],

        "BusinessType" : "",
"VehicleMakeCode":"31",


"GSTToState":"MAHARASHTRA",
"IsNoPrevInsurance":"true",

            "CustomerType":str( POST["CustomerType"]).upper(),


"IsLegalLiabilityToPaidDriver":"TRUE",
"IsTransferOfNCB":"false",

"CustomerDetails":{
            "CustomerType":str( POST["CustomerType"]).upper(),
"CustomerName": POST["CustomerName"],
"DateOfBirth": POST["DateOfBirth"],
"PinCode": POST["PinCode"],
"PANCardNo": POST["PANCardNo"],
"Email": POST["Email"],
"MobileNumber": POST["MobileNumber"],
"AddressLine1": POST["AddressLine1"],
"CountryCode":"100",
"StateCode": POST["StateCode"],
"CityCode": POST["CityCode"],

"GSTDetails":{
"CustomerType":str( POST["GSTCustomerType"]),
"ConstitutionOfBusiness": POST["ConstitutionOfBusiness"],
"GSTToState":"MAHARASHTRA",
"PanDetails": POST["PANCardNo"],
"GSTRegistrationStatus": POST["GSTRegistrationStatus"],
"GSTInNumber": POST["GSTInNumber"]
}
},

            "RTOLocationCode": POST["RTOLocationCode"],
            "ManufacturingYear": '',
"Tenure" : "1",
"TPTenure" : "5",
"PACoverTenure":"5",
"DealId" : "DL-3005/411041",
"BusinessType" : "",
"VehicleMakeCode" : "31",
        "DeliveryOrRegistrationDate": POST["reg_date"],
        "FirstRegistrationDate": POST["reg_date"],

        "PolicyStartDate": POST["new_date"],
        "PolicyEndDate": POST["new_date"],
        "GSTToState":str("MAHARASHTRA").upper(),
            "ExShowRoomPrice": POST["ExShowRoomPrice"],
            "CustomerType":str(POST["CustomerType"]),
"CorrelationId":str(uuid.uuid4()),
"paCoverForUnNamedPassenger": 0,
"paCoverForOwnerDriver": 100000,
}


    OldPolicy = POST["OldPolicy"]
    k["ManufacturingYear"] = k["FirstRegistrationDate"][:4]
    end_date = datetime.datetime.strptime(k["PolicyStartDate"], "%d/%m/%Y").date()
    end_date = str(end_date + datetime.timedelta(int(k["Tenure"]) * 364))
    k["PolicyEndDate"] = str(end_date)


    if OldPolicy == "false":
        k["BusinessType"] = "New Business"

    if OldPolicy == "true":
        k["BusinessType"] = "Roll Over"

    k["CustomerType"] = "Individual"
    k["PolicyStartDate"] = datetime.datetime.strptime(k["PolicyStartDate"], "%d/%m/%Y").strftime("%Y-%m-%d")


    return k

































    k = {
"RegistrationNumber":"MH02CF3063",
"EngineNumber":"ZDTT001012444",
"ChassisNumber":"CD01ZHN5410000",
"VehicleDescription":"test vehicle",
"VehicleModelCode":"380",
"RTOLocationCode":"192",
"ManufacturingYear":"2017",
"ExShowRoomPrice":"73689",
"DealId":"DL-3005/1483341",
"PolicyStartDate":"2017-07-16",
"PolicyEndDate":"2019-07-15",
"BusinessType":"New Business",
"VehicleMakeCode":"31",
"Tenure":"1",
"DeliveryOfRegistrationDate":"2018/04/27",
"FirstRegistrationDate":"2017/10/20",
"GSTToState":"MAHARASHTRA",
"IsNoPrevInsurance":"true",

"CustomerType":"INDIVIDUAL",
"IsLegalLiabilityToPaidDriver":"true",
"IsTransferOfNCB":"false",
"CorrelationId":"fe1c499f-0e64-4bdc-93a0-e29f8709a2c2",
"CustomerDetails":{
"CustomerType":"Individual",
"CustomerName":"test user13",
"DateOfBirth":"1989/12/16",
"PinCode":"400007",
"PANCardNo":"PQDAD1221A",
"Email":"test113@testing.com",
"MobileNumber":"9999977776",
"AddressLine1":"test area, test nagar1",
"CountryCode":"100",
"StateCode":"55",
"CityCode":"147",
"GSTDetails":{
"CustomerType":"RELATED PARTIES",
"ConstitutionOfBusiness":"PROPRIETORSHIP",
"GSTToState":"MAHARASHTRA",
"PanDetails":"PQDAD1221A",
"GSTRegistrationStatus":"TO BE COMMENCED",
"GSTInNumber":"01PQDAD1221ASDD"}
},
"ManufacturingYear" : "2017",
"Tenure" : "1",
"TPTenure" : "5",
"ExShowRoomPrice" : "73689",
"DealId" : "DL-3005/411041",
"BusinessType" : "New Business",
"VehicleMakeCode" : "31",
"DeliveryOrRegistrationDate" : "2018/09/02",
"PolicyStartDate" : "2018/09/19",
"PolicyEndDate" : "2019/09/18",
"GSTToState" : "MAHARASHTRA",
"CustomerType" : "INDIVIDUAL",
"CorrelationId":str(uuid.uuid4()),
"paCoverForUnNamedPassenger": 0,
"paCoverForOwnerDriver": 100000,
"PACoverTenure":"5",
}










def threesend1(request):
    """k={"CorrelationID": request.POST["correlation_id"],
            "BusinessType": request.POST["business_type"],
            "DealId": request.POST["deal_id"],
            "VehicleMakeCode": request.POST["vehical_make_code"],
            "VehicleModelCode": request.POST["vehical_model_code"],
            "VehicleDescription": request.POST["vehical_description"],
            "RTOLocationCode": request.POST["rto_location_code"],
            "ExShowRoomPrice": request.POST["ex_showroom_price"],
            "IsNoPrevInsurance": request.POST["is_no_prev_insurance"],
            "Tenure": request.POST["tenure"],
            "ManufacturingYear": request.POST["manufacturing_year"],
            "DeliveryOrRegistrationDate": request.POST["delivery_or_registration_date"],
            "FirstRegistrationDate": request.POST["first_registration_date"],
            "IsTransferOfNCB": request.POST["is_transfer_of_ncb"],
            "TransferOfNCBPercent": float(request.POST["transfer_of_ncb_percent"]),
            "BonusOnPreviousPolicy": request.POST["bonus_on_previous_policy"],
            "PreviousPolicyStartDate": request.POST["previous_policy_start_date"],
            "PreviousPolicyEndDate": request.POST["previous_policy_end_date"],
            "PreviousPolicynumber": request.POST["previous_policy_number"],
            "ClaimOnPreviousPolicy": request.POST["claim_on_previous_policy"],
            "TotalNoOfODIClaims": request.POST["total_no_of_od_claims"],
            "PreviouslyPolicyType": request.POST["previous_policy_type"],
            "PreviousInsuranceName": request.POST["previous_insurance_name"],
            "PreviousPolicyNumber": request.POST["previous_policy_number"],
            #"PreviousPolicySaleDate": request.POST["previous_policy_sale_date"],
            "PreviousVehicleSaleDate": request.POST["previous_policy_tenure"],
            "PreviousPolicyTenure": request.POST["previous_policy_tenure"],
            "PolicyStartDate": request.POST["policy_start_date"],
            "PolicyEndDate": request.POST["policy_end_date"],
            "CustomerType": request.POST["customer_type"],
            "IsHaveElectricalAccessories": request.POST["is_have_electrical_accessories"],
            "SIHaveElectricalAccessories": request.POST["si_have_electrical_accessories"],
            "IsHaveNonElectricalAccessories": request.POST["is_have_non_electrical_accessories"],
            "SIHaveNonElectricalAccessories": request.POST["si_have_non_electrical_accessories"],
            "TPPDLimit": request.POST["tppd_limit"],
            "IsLegalLiabilityToPaidDriver": request.POST["is_legal_liability_to_paid_driver"],
            "IsLegalLiabilityToPaidEmpolyee": request.POST["is_legal_liability_to_paid_empolyee"],
            "NoOfEmpolyee": request.POST["no_of_empolyee"],
            "IsPACoverUnnamedPassenger": request.POST["is_pa_cover_unnamed_passenger"],
            "SIPACoverUnnamedPassenger": request.POST["sipa_cover_unnamed_passenger"],
            "IsValidDrivingLicense": request.POST["is_valid_driving_licence"],
            "IsMoreThanOneVehicle": request.POST["is_more_than_one_vehical"],
            "IsPACoverOwnerDriver": request.POST["is_pa_cover_owner_driver"],
            "IsVoluntaryDeductible": request.POST["is_voluntary_deductible"],
            "VoluntaryDeductiblePlanName": request.POST["voluntry_deductible_plan_name"],
            "IsAutomobileAssocnFlag": request.POST["is_automobile_assocn_flag"],
            "AutomobileAssociationNumber": request.POST["automobile_association_number"],
            "IsAntiTheftDisc": request.POST["is_anti_theft_disk"],
            "IsHandicapDisc": request.POST["is_handicap_disk"],
            "IsExtensionCountry": request.POST["is_extension_country"],
            "ExtensionCountryName":request.POST["extension_country_name"],
            "ZeroDepPlanName": request.POST["zero_dep_plan_name"],
            "IsRTIApplicableFlag": request.POST["is_rti_applicable_flag"],
            #"IsConsumables": request.POST["is_consumables"],
            #"IsEngineProtectPlus": request.POST["is_engine_protect_plus"],
            "RSAPlanName": request.POST["rsa_plan_name"],
            "OtherLoading": float(request.POST["other_loading"]),
            "OtherDiscount": float(request.POST["other_discount"]),
            "EngineNumber": request.POST["engine_number"],
            "ChassisNumber": request.POST["chassis_number"],
            "RegistrationNumber": request.POST["registration_number"],
            "NameOfNominee": request.POST["name_of_nominee"],
            "Age": request.POST["age"],
            "NomineeType": request.POST["nominee_type"],
            "Relationship": request.POST["relationship"],
            "CustomerTypes": request.POST["customer_type"],
            "CustomerName": request.POST["customer_name"],
            "DateOfBirth": request.POST["date_of_birth"],
            "PinCode": request.POST["pin_code"],
            "PANCardNumber": request.POST["pan_card_number"],
            "Email": request.POST["email"],
            "MobileNumber": request.POST["mobile_number"],
            "AddressLine1": request.POST["address_line_1"],
            "CountryCode": request.POST["country_code"],
            "StateCode": request.POST["state_code"],
            "CityCode": request.POST["city_code"],
            "Gender": request.POST["gender"],
            "MobileISD": request.POST["mobile_isd"],
            "GSTExemptionApplicable": request.POST["gst_exemption_applicable"],
            "GSTInNumber": request.POST["gst_in_number"],
            "GSTToState": request.POST["gstto_state"],
            "ConstituationOfBusiness": request.POST["constituation_of_business"],
            "CustomerType": request.POST["gcustomer_type"],
            "PanDetail": request.POST["pan_detail"],
            "GSTRegistrationStatus": request.POST["gst_registration_status"],
            "FinancierName": request.POST["financier_name"],
            "BrandName": request.POST["brand_name"],
            "AgreementType": request.POST["agreement_type"],

            }"""
    try:
        POST = json.loads(request.GET.get("data"))
    except:
        POST = request.GET
    k = {
            "BusinessType": "Roll Over",
            "DealId": "DL-3005/1483341",
            "VehicleMakeCode": str(int(31)),
            "VehicleModelCode":str(int(POST["VehicleModelCode"])),
        "DeliveryOrRegistrationDate": POST["FirstRegistrationDate"],
        "FirstRegistrationDate": POST["FirstRegistrationDate"],

        "PolicyStartDate": POST["FirstRegistrationDate"],
        "PolicyEndDate": POST["FirstRegistrationDate"],

        "ManufacturingYear": '',
        "Tenure": "1",
            "ExShowRoomPrice": str(int(float( POST["ExShowRoomPrice"]))),
"GSTToState":"MAHARASHTRA",
"CustomerType" : POST["CustomerType"],
            "RTOLocationCode": POST["RTOLocationCode"],
            "IsNoPrevInsurance": "false",
                        "CorrelationId":str(uuid.uuid4()),


"IsPACoverOwnerDriver":"TRUE",
            "IsPACoverUnnamedPassenger": "FALSE",


"RegistrationNumber": POST["RegistrationNumber"],
"EngineNumber": POST["EngineNumber"],
"ChassisNumber": POST["ChassisNumber"],
"VehicleDescription": POST["VehicleDescription"],




"DealId":"DL-3005/1483341",
        "DeliveryOrRegistrationDate": POST["FirstRegistrationDate"],
        "FirstRegistrationDate": POST["FirstRegistrationDate"],

        "PolicyStartDate": POST["FirstRegistrationDate"],
        "PolicyEndDate": POST["FirstRegistrationDate"],

        "BusinessType" : "",
"VehicleMakeCode":"31",


"GSTToState":"MAHARASHTRA",
"IsNoPrevInsurance":"true",

            "CustomerType":str( POST["CustomerType"]).upper(),


"IsLegalLiabilityToPaidDriver":"TRUE",
"IsTransferOfNCB":"false",

"CustomerDetails":{
            "CustomerType":str( POST["CustomerType"]).upper(),
"CustomerName": POST["CustomerName"],
"DateOfBirth": POST["DateOfBirth"],
"PinCode": POST["PinCode"],
"PANCardNo": POST["PANCardNo"],
"Email": POST["Email"],
"MobileNumber": POST["MobileNumber"],
"AddressLine1": POST["AddressLine1"],
"CountryCode":"100",
"StateCode": POST["StateCode"],
"CityCode": POST["CityCode"],

"GSTDetails":{
"CustomerType":str( POST["GSTCustomerType"]),
"ConstitutionOfBusiness": POST["ConstitutionOfBusiness"],
"GSTToState":"MAHARASHTRA",
"PanDetails": POST["PANCardNo"],
"GSTRegistrationStatus": POST["GSTRegistrationStatus"],
"GSTInNumber": POST["GSTInNumber"]
}
},

            "RTOLocationCode": POST["RTOLocationCode"],
            "ManufacturingYear": '',
"Tenure" : "1",
"TPTenure" : "5",
"PACoverTenure":"5",
"DealId" : "DL-3005/411041",
"BusinessType" : "",
"VehicleMakeCode" : "31",
        "DeliveryOrRegistrationDate": POST["FirstRegistrationDate"],
        "FirstRegistrationDate": POST["FirstRegistrationDate"],

        "PolicyStartDate": POST["FirstRegistrationDate"],
        "PolicyEndDate": POST["FirstRegistrationDate"],
        "GSTToState":str("MAHARASHTRA").upper(),
            "ExShowRoomPrice": POST["ExShowRoomPrice"],
            "CustomerType":str(POST["CustomerType"]),
"CorrelationId":str(uuid.uuid4()),
"paCoverForUnNamedPassenger": 0,
"paCoverForOwnerDriver": 100000,
}


    old_policy = POST["old_policy"]
    k["ManufacturingYear"] = k["FirstRegistrationDate"][:4]
    end_date = datetime.datetime.strptime(k["PolicyStartDate"], "%Y-%m-%d").date()
    end_date = str(end_date + datetime.timedelta(int(k["Tenure"]) * 364))
    k["PolicyEndDate"] = str(end_date)


    if old_policy == "false":
        k["BusinessType"] = "New Business"

    if old_policy == "true":
        k["BusinessType"] = "Roll Over"

    k["CustomerType"] = "Individual"
    k["PolicyStartDate"] = datetime.datetime.strptime(k["PolicyStartDate"], "%Y-%m-%d").strftime("%Y-%m-%d")


    return k





