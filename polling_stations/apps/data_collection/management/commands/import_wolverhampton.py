from data_collection.morph_importer import BaseMorphApiImporter


class Command(BaseMorphApiImporter):

    srid = 4326
    districts_srid = 4326
    council_id = 'E08000031'
    elections = ['parl.2017-06-08']
    scraper_name = 'wdiv-scrapers/DC-PollingStations-Wolverhampton'
    geom_type = 'geojson'

    def district_record_to_dict(self, record):
        poly = self.extract_geometry(
            record,
            self.geom_type,
            self.get_srid('districts')
        )

        return {
            'internal_council_id': record['DIS_CODE'],
            'name': record['WARD'] + ' - ' + record['DIS_CODE'],
            'area': poly,
            'polling_station_id': record['DIS_CODE'],
        }

    def station_record_to_dict(self, record):
        location = self.extract_geometry(
            record,
            self.geom_type,
            self.get_srid('stations')
        )
        codes = record['DIS_CODE'].split(',')
        codes = [code.strip() for code in codes]

        stations = []
        for code in codes:
            stations.append({
                'internal_council_id': code,
                'address': record['ADDRESS'],
                'postcode': record['POSTCODE'],
                'location': location,
            })
        return stations
