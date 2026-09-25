from pydantic import  BaseModel, Field, ConfigDict

class GetSeniorityArguments(BaseModel):
    model_config = ConfigDict(strict=True)
    years_of_experience: int = Field(ge=0)


class CalculateYearsUntilSeniorArguments(BaseModel):
    model_config = ConfigDict(strict=True)
    years_of_experience: int = Field(ge=0)


class GetSkillCategoryArguments(BaseModel):
    model_config = ConfigDict(strict=True)
    skill: str = Field(min_length=1)


class CalculateResumeScoreArguments(BaseModel):
    model_config = ConfigDict(strict=True)
    years_of_experience: int = Field(ge=0)
    skills_count: int = Field(ge=0)
    has_projects: bool = Field(default=False)