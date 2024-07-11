import typing

def exceptionWrapper(*exceptions: typing.List[Exception], function: typing.Callable[..., any] = None) -> typing.Callable[[typing.Callable[..., any]], typing.Callable[..., any]]:
    def functionWrapper(function: typing.Callable[..., any], ) -> typing.Callable[..., any]:
        def sampledExceptionFunction(*args, **kwargs):
            try:
                return function(*args, **kwargs)
            except tuple(exceptions) as excp:
                if function != None:
                    function(excp)
                    pass
                raise Exception(f"Raised exception {type(excp).__name__} with arguments: {str(excp)}") from None
        
        return sampledExceptionFunction
    return functionWrapper