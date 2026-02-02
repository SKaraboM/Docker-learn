import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as f:
    yaml_data = yaml.safe_load(f)
 
    rss_El = xml_tree.Element('rss', {
        'version':'2.0',
        'xmlns:itunes':'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content':'http://purl.org/rss/1.0/modules/content/'
    })
channelEl = xml_tree.SubElement(rss_El, 'channel')
link_pre = yaml_data['link']
xml_tree.SubElement(channelEl, 'title').text = yaml_data['title']
xml_tree.SubElement(channelEl, 'description').text = yaml_data['description']
xml_tree.SubElement(channelEl, 'itunes:author').text = yaml_data['author']
xml_tree.SubElement(channelEl, 'itunes:image', {'href': link_pre + yaml_data['image']})
xml_tree.SubElement(channelEl, 'link', {'href': link_pre})
for item in yaml_data['item']:
    item_el = xml_tree.SubElement(channelEl, 'item')
    xml_tree.SubElement(item_el, 'title').text =  item['title']
    xml_tree.SubElement(item_el, 'description').text =  item['description']

    enclosure = xml_tree.SubElement(item_el, 'enclosure', {
        'url':link_pre + item['file'],
        'type':'audio/mpeg',
        'lenght': item['length']
    })
output = xml_tree.ElementTree(rss_El)
output.write("podcast.xml", encoding='UTF-8', xml_declaration=True)


    
