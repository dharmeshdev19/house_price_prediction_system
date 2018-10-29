from sklearn.externals import joblib
from model import DBModel


class ModelPrediction(object):
    def __init__(self):
        pass

    '''Takes user input and makes house price prediction '''
    def make_prediction(self, house_data):
        # format the data

        formated_data = [self.format_input_data(house_data)]

        # Load the model we trained previously
        model = joblib.load('trained_house_prediction_model.pkl')

        # Run the model and make a prediction for each house in the homes_to_value array
        predicted_home_values = model.predict(formated_data)

        # Since we are only predicting the price of one house, just look at the first prediction returned
        predicted_value = int(round(predicted_home_values[0]))

        output = self.design_output(house_data, predicted_value)

        return output


    # end of method


    ''' Method to format the data as required by the scikit library'''
    def format_input_data(self, house_data):
        formated_data = [
            house_data['num_bedrooms'],  # num_of_bhk
            house_data['total_sqft'],  # total_sqft
            house_data['livable_sqft'],  # livable_sqft
            house_data['num_bedrooms'],  # num_bedrooms
            house_data['num_bathrooms'],  # num_bathrooms
            house_data['flat_condition'],  # flat_condition
            house_data['flooring_type'],  # flooring_type
            house_data['parking'],  # parking
            house_data['furnishing_state'],  # furnishing_state
            house_data['year_built'],  # year_built
            house_data['location'],  # location
            house_data['property_on_num'],  # property_on_num
        ]

        return formated_data
    # end of method

    def design_output(self,house_data, predicted_value):

        db_model_obj = DBModel()


        output = """ You have provided below data <br> 
                      Total Area: {}  <br>
                      Livable Area: {} <br>
                      Number of Bedrooms: {} <br>
                      Number of Bathrooms: {} <br>
                      Flat Condition: {} <br>
                      Flooring Type: {} <br>
                      Parking Available: {} <br>
                      Furnishing State: {} <br>
                      Year Built: {} <br>
                      Location: {} <br>
                      Propery Floor Number: {} <br><br><br>
                
                """.format(house_data['total_sqft'],house_data['livable_sqft'],house_data['num_bedrooms'],house_data['num_bathrooms'], db_model_obj.select_db_data('flat_condition_master',house_data['flat_condition']), db_model_obj.select_db_data('flooring_type_master',house_data['flooring_type']), db_model_obj.select_db_data('parking_master',house_data['parking']), db_model_obj.select_db_data('furnishing_state_master',house_data['furnishing_state']), db_model_obj.select_db_data('year_built_master',house_data['year_built']), db_model_obj.select_db_data('location_master',house_data['location']),house_data['property_on_num'])



        output += "For above scenario the house/flat has an estimated value of {}".format(self.format_house_value(predicted_value))

        return output
    # end of method

    def format_house_value(self, value):
        # first calculate the length of the house
        value_len = len(str(value))

        new_value = 0

        if value_len > 7:
            new_value = str(round(value / 10000000, 2)) + " Crores"
        elif value_len == 7:
            new_value = str(round(value / 1000000, 2)) + " Lakhs"
        elif value_len == 6:
            new_value = str(round(value / 100000, 2)) + " Lakh"

        return new_value

    # end of method

# end of class definition