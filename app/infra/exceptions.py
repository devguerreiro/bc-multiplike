from fastapi.responses import JSONResponse


class BadRequestException(JSONResponse):
    def __init__(self, e: Exception) -> None:
        super().__init__(content={"error": str(e)}, status_code=400)


class NotFoundException(JSONResponse):
    def __init__(self, msg: str) -> None:
        super().__init__(content={"error": msg}, status_code=404)
