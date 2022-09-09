from application.domain.adverts import Advert
from application.services.database import pg_adapter
from application.services.file_storage import file_storage


def create_advert(user_id, title, description, price, advert_files):
	advert = Advert(title, description, price)
	advert.set_creation_date()
	advert.set_expiration_date(60*60*24)

	advert_photos = advert_files.to_dict(flat=False)["create-adv-files"]
	print(advert_photos)
	
	pg = pg_adapter()

	advert_id = pg.add_advert(advert, user_id)

	if advert_id:
		storage = file_storage()

		filenames, filesizes = storage.save_photos(advert_photos, advert_id)

		pg.save_photos(filenames, filesizes, advert_id)
	
	return advert_id


def get_user_adverts(user_id):
	pg = pg_adapter()

	adverts = pg.get_users_adverts(user_id)

	return adverts
