from langchain_core.prompts import PromptTemplate

#Template
template = PromptTemplate(
    template="""
Please compare cricketer "{player_input}" with Rohit Sharma based on following aspects:
Based on : {compare_input}
in "{format_input}"
1. Statistical Comparison:
    -Include proper stats till data availabe to you that is available for the {compare_input} for the {format_input} format
    -Explain in simple terms to the users, telling who perform better statistically and give comparison tables
2. Similarity:
    -Include what is similar in them in the give aspect {compare_input} for the {format_input} format
you can also tell who is more pleasing to eyes while batting and who have that extra bit of the time for his batting
Ensure comparison is clear, accurate, based on data and facts till data available to you in the provided format and aspect.
Also clearly mention the time period for which you have used the stats
""",
input_variables=['player_input', 'format_input', 'compare_input'],
validate_template=True
)

template.save('template.json')