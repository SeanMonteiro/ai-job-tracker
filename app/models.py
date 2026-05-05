from pydantic import BaseModel

class JobBase(BaseModel):
    title: str
    company: str
    description: str | None = None


class JobCreate(JobBase):
    pass


class JobResponse(JobBase):
    id: int