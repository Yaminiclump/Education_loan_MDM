

class errors():

    success = {'error_code':10000,'message':"Success"}

    #business error
    generic_error_1 = {'error_code': 20101, 'message': "Invalid request details"}
    generic_error_2 = {'error_code': 20102, 'message': "There was some error while processing the request"}
    invalid_request = {'error_code': 20103, 'message': "Invalid request method (only POST method is allowed)"}

    country_error_1 = {'error_code': 20001, 'message': "Could not find anything for the provided details"}
    state_error_1 = {'error_code': 20002, 'message': "Could not find anything for the provided details"}
    city_error_1 = {'error_code': 20003, 'message': "Could not find anything for the provided details"}
    pincode_error_1 = {'error_code': 20004, 'message': "Could not find anything for the provided details"}
    institute_error_1 = {'error_code': 20005, 'message': "Could not find anything for the provided details"}




