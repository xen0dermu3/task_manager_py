"""File that contains not found exception for the application."""

from uuid import UUID


class NotFoundException(Exception):
    """Not found exception for the application."""

    def __init__(self, item_id: UUID):
        self.item_id = item_id
