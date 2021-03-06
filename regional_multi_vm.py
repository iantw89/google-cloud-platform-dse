import yaml
import copy


def GenerateConfig(context):
    # YAML config.
    config = {'resources': []}

    # A zonal vm_multiple_instances resource for each zone in the properties list.
    for zone in context.properties['zones']:
        new_properties = copy.deepcopy(context.properties)
        new_properties["zone"] = zone
        service = {
            'name': context.env['deployment'] + '-service-' + zone,
            'type': 'gcp/vm_multiple_instances.py',
            'properties': new_properties
        }

        config['resources'].append(service)

    return yaml.dump(config)
