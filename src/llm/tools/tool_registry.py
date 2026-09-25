from llm.tools.tools import get_seniority, calculate_years_until_senior, get_skill_category, calculate_resume_score 
from tool_schema_model import ToolDefinition
from tool_arguments import    CalculateResumeScoreArguments, CalculateYearsUntilSeniorArguments, GetSeniorityArguments, GetSkillCategoryArguments


tool_registry: dict[str, ToolDefinition] = {
    "get_seniority": ToolDefinition(
        function= get_seniority,
        arguments_model= GetSeniorityArguments),
    "calculate_years_until_senior": ToolDefinition(
        function= calculate_years_until_senior,
        arguments_model= CalculateYearsUntilSeniorArguments),
    "get_skill_category": ToolDefinition(
        function= get_skill_category,
        arguments_model= GetSkillCategoryArguments),
    "calculate_resume_score": ToolDefinition(
        function= calculate_resume_score,
        arguments_model= CalculateResumeScoreArguments)
    
}