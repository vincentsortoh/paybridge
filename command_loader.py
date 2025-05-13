from loguru import logger
import importlib
from core.commands.generic_command import GenericCommand


def load_and_execute(provider_name, command_name, **kwargs):
    try:
        # Load provider
        provider_module = importlib.import_module(f"providers.{provider_name}.provider")
        ProviderClass = getattr(
            provider_module, f"{provider_name.capitalize()}Provider"
        )
        provider_instance = ProviderClass()

        mapper_instance = None

        try:
            mapper_module = importlib.import_module(
                f"providers.{provider_name}.param_mapper"
            )
            MapperClass = getattr(
                mapper_module, f"{provider_name.capitalize()}ParamMapper"
            )
            mapper_instance = MapperClass()
            mapped_kwargs = mapper_instance.map_parameters(command_name, kwargs)
            logger.info("mapped parameters {mapped_kwargs}")
        except ModuleNotFoundError:
            mapped_kwargs = kwargs


        try:
            command_module = importlib.import_module(
                f"providers.{provider_name}.commands.{command_name}"
            )
            class_name = (
                "".join(word.capitalize() for word in command_name.split("_"))
                + "Command"
            )
            CommandClass = getattr(command_module, class_name)
            result = CommandClass(provider_instance).execute(**mapped_kwargs)
        except ModuleNotFoundError:
            result = GenericCommand(provider_instance, command_name).execute(
                **mapped_kwargs
            )

        try:
            if mapper_instance is None:
                mapper_module = importlib.import_module(
                    f"providers.{provider_name}.param_mapper"
                )
                MapperClass = getattr(
                    mapper_module, f"{provider_name.capitalize()}ParamMapper"
                )
                mapper_instance = MapperClass()
                response_mapper = mapper_instance.map_response(command_name, result)
            else:
                response_mapper = mapper_instance.map_response(command_name, result)

            return response_mapper
        
        except ModuleNotFoundError:
            return result

    except Exception as e:
        raise Exception(f"Error: {e}")
