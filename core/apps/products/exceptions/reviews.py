from dataclasses import dataclass

from core.apps.common.exceptions import ServiceException


@dataclass(eq=False)
class ReviewInvalidRatingException(ServiceException):
    rating: int

    @property
    def message(self):
        return "Review rating is not valid"
