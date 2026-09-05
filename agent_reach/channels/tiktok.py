# -*- coding: utf-8 -*-
"""TikTok — OpenCLI backend using the user's logged-in Chrome session."""

from ._opencli_site import OpenCLISiteChannel


class TikTokChannel(OpenCLISiteChannel):
    name = "tiktok"
    description = "TikTok 视频搜索、用户主页和推荐流"
    site = "tiktok"
    domains = ("tiktok.com", "vm.tiktok.com", "vt.tiktok.com")
    usage = "opencli tiktok search/user/profile/explore -f yaml"
    login_hint = "tiktok.com"
