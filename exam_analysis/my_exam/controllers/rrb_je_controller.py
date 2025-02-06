from bs4 import BeautifulSoup
import requests

class RRBJEController:
    @staticmethod
    def fetch_exam_data(url: str):
        """
        Function to scrape data from the given URL.
        This function fetches the HTML content of the URL and extracts the required exam data.
        """
        try:
            # Send the HTTP request to the URL
            response = requests.get(url)
            
            # Check if the request was successful
            if response.status_code == 200:
                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, "html.parser")
                
                # Extract the first table (exam details) - Make sure the table exists
                table = soup.find('table', {'border': '1'})
                if table:
                    rows = table.find_all('tr')
                    exam_data = {}
                    
                    for row in rows:
                        columns = row.find_all('td')
                        if len(columns) > 1:  # Check if there are at least two columns in the row
                            key = columns[0].get_text(strip=True)
                            value = columns[1].get_text(strip=True)
                            exam_data[key] = value
                    
                    # Extract the questions and answers section
                    questions = soup.find_all('div', class_='question-pnl')
                    correct_count = 0
                    wrong_count = 0
                    not_attempted_count = 0
                    
                    for question in questions:
                        question_data = {}
                        question_text = question.find('td', class_='bold')
                        if question_text:
                            question_data['question'] = question_text.text.strip()

                        # Extract the answer choices and check if the user has selected an option
                        chosen_option_tag = question.find('td', text="Chosen Option :")
                        if chosen_option_tag:
                            chosen_option_value = chosen_option_tag.find_next('td').text.strip()
                        else:
                            chosen_option_value = None
                        if chosen_option_value == '--' or not chosen_option_value:
                            chosen_option_number = None
                        else:
                            chosen_option_number = chosen_option_value.split('.')[0].strip() if chosen_option_value else None
                        correct_answer_tag = question.find('td', class_='rightAns')
                        if correct_answer_tag:
                            correct_answer_value = correct_answer_tag.get_text(strip=True)
                        else:
                            correct_answer_value = None
                        # Extract just the option number for both the chosen and correct answers
                        correct_answer_number = correct_answer_value.split('.')[0].strip() if correct_answer_value else None
                        
                            
                        print(f"Chosen Option: '{chosen_option_number}'")
                        print(f"Correct Answer: '{correct_answer_number}'")
                        if chosen_option_number == correct_answer_number:
                            correct_count += 1
                        elif chosen_option_number and chosen_option_number != correct_answer_number:  # If the answer was chosen but incorrect
                            wrong_count += 1
                        else:
                            not_attempted_count += 1
                    
                    # Return the exam data along with right, wrong, and not attempted counts
                    extracted_data = {
                        'exam_data': exam_data,
                        'right_answers': correct_count,
                        'wrong_answers': wrong_count,
                        'not_attempted': not_attempted_count
                    }
                    return extracted_data
                else:
                    return {"error": "Exam details table not found."}
            else:
                return {"error": f"Failed to retrieve content. Status Code: {response.status_code}"}
        
        except Exception as e:
            return {"error": f"An error occurred: {str(e)}"}
