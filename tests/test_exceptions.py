from pyhttptest import exceptions


def test_file_extension_error_exception():
    file_extension_error = exceptions.FileExtensionError('.yaml')
    exception_message = (
        "A file extension '.yaml' is not supported. "
        "Only a file with '.json' extension is supported"
    )

    assert file_extension_error.message == exception_message


def test_http_method_not_supported_error_exception():
    http_method_not_supported_error = exceptions.HTTPMethodNotSupportedError('HEAD')
    exception_message = "An HTTP method ('HEAD') is not supported by the application."

    assert http_method_not_supported_error.message == exception_message
