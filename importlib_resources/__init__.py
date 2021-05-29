"""Read resources contained within a package."""

from ._common import (
    as_file,
    files,
    contents,
    open_binary,
    read_binary,
    open_text,
    read_text,
    is_resource,
    path,
    Package,
    Resource,
)

from importlib_resources.abc import ResourceReader


__all__ = [
    'Package',
    'Resource',
    'ResourceReader',
    'as_file',
    'contents',
    'files',
    'is_resource',
    'open_binary',
    'open_text',
    'path',
    'read_binary',
    'read_text',
]
