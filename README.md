"# Selenium-BDD-with-POM" 
"# Selenium-BDD-with-POM" 

--Run the command to execute specific feature files:--
behave -f allure_behave.formatter:AllureFormatter -o allure-results features/Elements.feature features/Element_Attributes.feature

--Generate the Allure report after execution:--
allure serve allure-results
