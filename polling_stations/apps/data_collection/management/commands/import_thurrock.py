from data_collection.management.commands import BaseXpressDemocracyClubCsvImporter

class Command(BaseXpressDemocracyClubCsvImporter):
    council_id = 'E06000034'
    addresses_name = 'parl.2017-06-08/Version 1/Democracy_Club__08June2017 (8).tsv'
    stations_name = 'parl.2017-06-08/Version 1/Democracy_Club__08June2017 (8).tsv'
    elections = ['parl.2017-06-08']
    csv_delimiter = '\t'

    def station_record_to_dict(self, record):

        """
        File supplied contained obviously inaccurate point
        remove it and fall back to geocoding
        """
        if record.polling_place_id == '4871':
            record = record._replace(polling_place_easting = '0')
            record = record._replace(polling_place_northing = '0')

        return super().station_record_to_dict(record)
