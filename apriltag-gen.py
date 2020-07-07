import numpy as np
import cv2
from fpdf import FPDF
from pathlib import Path, PurePosixPath
from pathlib import PurePosixPath

tag_path = 'apriltag-imgs/tag36h11/'
tag_pattern = 'tag36_11_*.png'
#tag_pattern = 'tag36_11_00000.png'

resized_tags_folder = 'tag36h11_big/'
ouput_folder = 'output/'

pathlist = Path(tag_path).rglob(tag_pattern)
for img_path in pathlist:
	# because path is object not string
	img_fn = str(img_path)

	bfn = PurePosixPath(img_fn).stem
	tagid = bfn.split('_')[2]

	# don't create resized image if already exists
	r_img_path = Path(resized_tags_folder + bfn + '.jpg')
	if (r_img_path.exists() == False):
		# load image
		img = cv2.imread(img_fn,0)

		# crop border
		crop_img = img[1:1+8, 1:1+8]

		# resize to something really big
		r_img = cv2.resize(crop_img,(2000,2000),fx=0, fy=0, interpolation = cv2.INTER_NEAREST)

		cv2.imwrite(str(r_img_path),r_img)

	# don't create pdf if already exists
	pdf_out_path = Path(ouput_folder + bfn + '.pdf')
	if (pdf_out_path.exists() == False):

		pdf=FPDF('P','mm','letter')
		pdf.set_font('Arial', 'B', 10)
		pdf.add_page()

		tagid_i = int(tagid)
		if (tagid_i <= 150):
			tag_size = 150
		elif (tagid_i <= 300):
			tag_size = 100
		elif (tagid_i <= 450):
			tag_size = 50
		else:
			tag_size = 20

		pdf.image(str(r_img_path), x=216/2-tag_size/2, y=279/2-tag_size/2, w=tag_size)
		pdf.set_xy(x=216/2-50, y=279/2+tag_size/2)
		pdf.cell(100, 5, 'tag 36h11 id:' + tagid, 0, 2, 'C')
		pdf.cell(100, 5, ' (' + str(tag_size) + 'x'+ str(tag_size) +' mm)', 0, 2, 'C')

		pdf.output(str(pdf_out_path))
