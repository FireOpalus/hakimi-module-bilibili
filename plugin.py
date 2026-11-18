"""Bilibili account and patrol integration."""

from hakimi.modules.bilibili import Bilibili
from hakimi.modules.bilibili_surf import BilibiliSurfModule


def create_module(service):
    module = BilibiliSurfModule(
        service.s,
        watcher=service.bili_watcher,
        bili=service.bili,
        node_transport=service.node_transport,
    )
    service.bili_watcher.module_enabled = lambda: module.inactive_reason is None
    if isinstance(service.bili, Bilibili):
        service.bili.module_enabled = service.bili_watcher.module_enabled
    return module
