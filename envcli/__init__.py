__app_name__ = "envcli"
__version__ = "0.0.1"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    DOKKU_ERROR,
    JSON_ERROR,
    ID_ERROR,
) = range(6)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "faild to read file",
    DOKKU_ERROR: "dokku error",
    ID_ERROR: "to-do id error",
}