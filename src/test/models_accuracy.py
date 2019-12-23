import json


def main():
    with open('./src/test/predictions.json', 'r') as f:
        data = json.load(f)
    
    total = len(data['label'])
    google = 0
    sphinx = 0
    for i in range(len(data['label'])):
        label = data['label'][i]
        google_entry = data['google'][i]
        sphinx_entry = data['pocket_sphinx'][i]

        if google_entry == label:
            google += 1
        if sphinx_entry == label:
            sphinx += 1
        
    print('Google %d out of %d: %.4f' %(google, total, google/total))
    print('Pocket Sphinx %d out of %d: %.4f' %(sphinx, total, sphinx/total))

if __name__ == "__main__":
    main()