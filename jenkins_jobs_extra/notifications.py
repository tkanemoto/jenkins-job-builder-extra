import xml.etree.ElementTree as XML

import jenkins_jobs.modules.helpers as helpers


def to_camel_case(snake_str, title_first=False):
    components = snake_str.split('-')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return (components[0].title() if title_first else components[0]) + ''.join(x.title() for x in components[1:])


def office365(registry, xml_parent, data):
  prop = XML.SubElement(xml_parent,
                        'jenkins.plugins.office365connector.'
                        'WebhookJobProperty')
  webhooks = XML.SubElement(prop, 'webhooks')
  supported_formats = ['JSON', 'XML']
  supported_events = ['started', 'completed', 'finalized', 'all']
  for hook_data in data.get('webhooks', []):
    webhook = XML.SubElement(webhooks,
                             'jenkins.plugins.office365connector.'
                             'Webhook')
    #fmt = hook_data.get('format', 'JSON').upper()
    #event = hook_data.get('event', 'all').lower()
    mapping = [
      ('name', 'name', None),
      ('timeout', 'timeout', 30000),
      ('url', 'url', None),
      ('start-notification', 'startNotification', 'false'),
    ]

    events = hook_data.get('events', {})
    for key in events.keys():
      mapping.append(
        ('', 'notify{}'.format(to_camel_case(key, True)), 'true' if events[key] else 'false')
      )

    helpers.convert_mapping_to_xml(
      webhook, hook_data, mapping, fail_required=True)
