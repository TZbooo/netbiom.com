from pydantic import BaseModel, HttpUrl, Field

from src.service import get_hex_uuid


class HyperLink(BaseModel):
    url: HttpUrl
    text: str


class SocialAccountsHyperLinks(BaseModel):
    instagram: HyperLink | None
    telegram: HyperLink | None
    github: HyperLink | None
    linkedin: HyperLink | None
    vk: HyperLink | None


class PageBase(BaseModel):
    title: str
    html_text: str
    social_accounts_hyper_links: SocialAccountsHyperLinks


class PageModel(PageBase):
    page_id: str = Field(default_factory=get_hex_uuid)


class PageCreate(PageBase):
    ...


class PageOut(PageModel):
    ...
