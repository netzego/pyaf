SOX			:= $(shell which sox)
LAME		:= $(shell which lame)
FLAC		:= $(shell which flac)
METAFLAC	:= $(shell which metaflac)
ID3V2		:= $(shell which id3v2)
XXD			:= $(shell which xxd)

ARTIST		:= "test_artist"
ALBUM		:= "test_album"
ALBUMARTIST	:= "test_albumartist"
COMMENT		:= "test_comment"
TITLE		:= "test_title"
YEAR		:= $(shell date +%Y)

EMPTY_DIR	:= empty
EMPTY_FLAC	:= $(EMPTY_DIR)/empty.flac
EMPTY_MP3	:= $(EMPTY_DIR)/empty.mp3
EMPTY_WAV	:= $(EMPTY_DIR)/empty.wav

NOTAGS_DIR	:= notags
NOTAGS_FLAC	:= $(NOTAGS_DIR)/notags.flac
NOTAGS_MP3	:= $(NOTAGS_DIR)/notags.mp3
NOTAGS_WAV	:= $(NOTAGS_DIR)/notags.wav

ID3V1_DIR	:= id3v1
ID3V1_MP3	:= $(ID3V1_DIR)/id3v1.mp3
ID3V1_WAV	:= $(ID3V1_DIR)/id3v1.wav

ID3V2_DIR	:= id3v2
ID3V2_MP3	:= $(ID3V2_DIR)/id3v2.mp3
ID3V2_WAV	:= $(ID3V2_DIR)/id3v2.wav

VORBIS_DIR	:= vorbis
VORBIS_FLAC	:= $(VORBIS_DIR)/vorbis.flac

SYMLNK_DIR	:= symlink

PERM_DIR	:= perm
PERM_000MP3	:= $(PERM_DIR)/0x000.mp3
PERM_110MP3	:= $(PERM_DIR)/0x110.mp3
PERM_220MP3	:= $(PERM_DIR)/0x220.mp3
PERM_440MP3	:= $(PERM_DIR)/0x440.mp3
PERM_000WAV	:= $(PERM_DIR)/0x000.wav
PERM_110WAV	:= $(PERM_DIR)/0x110.wav
PERM_220WAV	:= $(PERM_DIR)/0x220.wav
PERM_440WAV	:= $(PERM_DIR)/0x440.wav
PERM_000FLAC:= $(PERM_DIR)/0x000.flac
PERM_110FLAC:= $(PERM_DIR)/0x110.flac
PERM_220FLAC:= $(PERM_DIR)/0x220.flac
PERM_440FLAC:= $(PERM_DIR)/0x440.flac

EXT_DIR		:= ext
EXT_WRGMP3	:= $(EXT_DIR)/wrong_ext.mp3
EXT_WRGFLAC	:= $(EXT_DIR)/wrong_ext.flac
EXT_WRGWAV	:= $(EXT_DIR)/wrong_ext.wav
EXT_BIGFLAC	:= $(EXT_DIR)/caps_ext.FLAC
EXT_BIGMP3	:= $(EXT_DIR)/caps_ext.MP3
EXT_BIGWAV	:= $(EXT_DIR)/caps_ext.WAV

REC_DIR		:= recursiv
REC_DIR_A	:= $(REC_DIR)/abc
REC_DIR_AX	:= $(REC_DIR)/abc/xyz

COR_DIR		:= corrupt
# flac
MP31_H_FLAC	:= $(COR_DIR)/mp3v1_header.flac
MP32_H_FLAC	:= $(COR_DIR)/mp3v2_header.flac
WAV_H_FLAC	:= $(COR_DIR)/wav_header.flac
# mp3
FLAC_H_MP3	:= $(COR_DIR)/flac_header.mp3
WAV_H_MP3	:= $(COR_DIR)/wav_header.mp3
# wav
MP31_H_WAV	:= $(COR_DIR)/mp3v1_header.wav
MP32_H_WAV	:= $(COR_DIR)/mp3v2_header.wav
FLAC_H_WAV	:= $(COR_DIR)/flac_header.wav
# header bytes
HEADER_FLAC	:= 664c 6143
HEADER_MP31	:= fffb e444 0000 0000
HEADER_MP32	:= 4944 3303 0000 0000 
HEADER_WAV	:= 5249 4646 2477 0100 5741 5645

all: clean empty notags id3v1 id3v2 vorbis symlink perm ext recursiv corrupt

clean:
	fd --type d --max-depth 1 --no-ignore -x rm -r {}

empty:
	mkdir $(EMPTY_DIR)
	touch $(EMPTY_FLAC)
	touch $(EMPTY_MP3)
	touch $(EMPTY_WAV)

notags:
	mkdir $(NOTAGS_DIR)
	$(SOX) -c 2 -b 16 -n $(NOTAGS_WAV) synth 00:00.5 pinknoise
	$(FLAC) $(NOTAGS_WAV)
	$(LAME) -b 320 -h $(NOTAGS_WAV)

id3v1: notags
	mkdir $(ID3V1_DIR)
	cp $(NOTAGS_MP3) $(ID3V1_MP3)
	cp $(NOTAGS_WAV) $(ID3V1_WAV)
	$(ID3V2) -1 \
		-A $(ALBUM) \
		-a $(ARTIST) \
		-c $(COMMENT) \
		-t $(TITLE) \
		-y $(YEAR) \
		-T 1/1 \
		--TPOS 1/1 \
		--TPE2 $(ALBUMARTIST) \
		$(ID3V1_MP3)
	$(ID3V2) -1 \
		-A $(ALBUM) \
		-a $(ARTIST) \
		-c $(COMMENT) \
		-t $(TITLE) \
		-y $(YEAR) \
		-T 1/1 \
		--TPOS 1/1 \
		--TPE2 $(ALBUMARTIST) \
		$(ID3V1_WAV)

id3v2: notags
	mkdir $(ID3V2_DIR)
	cp $(NOTAGS_MP3) $(ID3V2_MP3)
	cp $(NOTAGS_WAV) $(ID3V2_WAV)
	$(ID3V2) -2 \
		-A $(ALBUM) \
		-a $(ARTIST) \
		-c $(COMMENT) \
		-t $(TITLE) \
		-y $(YEAR) \
		-T 1/1 \
		--TPOS 1/1 \
		--TPE2 $(ALBUMARTIST) \
		$(ID3V2_MP3)
	$(ID3V2) -2 \
		-A $(ALBUM) \
		-a $(ARTIST) \
		-c $(COMMENT) \
		-t $(TITLE) \
		-y $(YEAR) \
		-T 1/1 \
		--TPOS 1/1 \
		--TPE2 $(ALBUMARTIST) \
		$(ID3V2_WAV)

vorbis: notags
	mkdir $(VORBIS_DIR)
	cp $(NOTAGS_FLAC) $(VORBIS_FLAC)
	$(METAFLAC) \
		--set-tag=ARTIST=$(ARTIST) \
		--set-tag=ALBUM=$(ALBUM) \
		--set-tag=ALBUMARTIST=$(ALBUMARTIST) \
		--set-tag=COMMENT=$(COMMENT) \
		--set-tag=TITLE=$(TITLE) \
		--set-tag=YEAR=$(YEAR) \
		--set-tag=TRACKNUMBER=1 \
		--set-tag=TOTALTRACKS=1 \
		--set-tag=DISCNUMBER=1 \
		--set-tag=TOTALDISCS=1 \
		$(VORBIS_FLAC)

symlink: id3v2 vorbis
	mkdir $(SYMLNK_DIR)
	ln -s ../$(VORBIS_FLAC) $(SYMLNK_DIR)
	ln -s ../$(ID3V1_WAV) $(SYMLNK_DIR)
	ln -s ../$(ID3V2_WAV) $(SYMLNK_DIR)
	ln -s ../$(ID3V1_MP3) $(SYMLNK_DIR)
	ln -s ../$(ID3V2_MP3) $(SYMLNK_DIR)
	ln -s ../$(ID3V2_DIR) $(SYMLNK_DIR)
	ln -s ../$(ID3V1_DIR) $(SYMLNK_DIR)
	ln -s ../$(VORBIS_DIR) $(SYMLNK_DIR)

perm: id3v2 vorbis
	mkdir $(PERM_DIR)
	@# flac files
	cp $(VORBIS_FLAC) $(PERM_000FLAC)
	chmod 000 $(PERM_000FLAC)
	cp $(VORBIS_FLAC) $(PERM_110FLAC)
	chmod 110 $(PERM_110FLAC)
	cp $(VORBIS_FLAC) $(PERM_220FLAC)
	chmod 220 $(PERM_220FLAC)
	cp $(VORBIS_FLAC) $(PERM_440FLAC)
	chmod 440 $(PERM_440FLAC)
	@# mp3 files
	cp $(ID3V2_MP3) $(PERM_000MP3)
	chmod 000 $(PERM_000MP3)
	cp $(ID3V2_MP3) $(PERM_110MP3)
	chmod 110 $(PERM_110MP3)
	cp $(ID3V2_MP3) $(PERM_220MP3)
	chmod 220 $(PERM_220MP3)
	cp $(ID3V2_MP3) $(PERM_440MP3)
	chmod 440 $(PERM_440MP3)
	@# wav files
	cp $(ID3V1_WAV) $(PERM_000WAV)
	chmod 000 $(PERM_000WAV)
	cp $(ID3V1_WAV) $(PERM_110WAV)
	chmod 110 $(PERM_110WAV)
	cp $(ID3V1_WAV) $(PERM_220WAV)
	chmod 220 $(PERM_220WAV)
	cp $(ID3V1_WAV) $(PERM_440WAV)
	chmod 440 $(PERM_440WAV)

ext: id3v2 vorbis
	mkdir $(EXT_DIR)
	@# Worng extension for id3v2.mp3
	cp $(ID3V2_MP3) $(EXT_WRGMP3).flac
	cp $(ID3V2_MP3) $(EXT_WRGMP3).wav
	cp $(ID3V2_MP3) $(EXT_WRGMP3).txt
	@# Worng extension for id3v2.flac
	cp $(VORBIS_FLAC) $(EXT_WRGFLAC).mp3
	cp $(VORBIS_FLAC) $(EXT_WRGFLAC).wav
	cp $(VORBIS_FLAC) $(EXT_WRGFLAC).txt
	@# Worng extension for id3v2.wav
	cp $(ID3V1_WAV) $(EXT_WRGWAV).flac
	cp $(ID3V1_WAV) $(EXT_WRGWAV).mp3
	cp $(ID3V1_WAV) $(EXT_WRGWAV).txt
	@# Big written extension
	cp $(VORBIS_FLAC) $(EXT_BIGFLAC)
	cp $(ID3V2_MP3) $(EXT_BIGMP3)
	cp $(ID3V1_WAV) $(EXT_BIGWAV)

corrupt: notags
	@# https://askubuntu.com/a/1034380
	mkdir $(COR_DIR)

	@# wav_header.flac
	cp $(NOTAGS_FLAC) $(WAV_H_FLAC)
	$(XXD) -r -p -o 0 <(echo $(HEADER_WAV)) $(WAV_H_FLAC)
	@# mp3v1_header.flac
	cp $(NOTAGS_FLAC) $(MP31_H_FLAC)
	$(XXD) -r -p -o 0 <(echo $(HEADER_MP31)) $(MP31_H_FLAC)
	@# mp3v2_header.flac
	cp $(NOTAGS_FLAC) $(MP32_H_FLAC)
	@$(XXD) -r -p -o 0 <(echo $(HEADER_MP32)) $(MP32_H_FLAC)

	@# flac_header.mp3
	cp $(NOTAGS_MP3) $(FLAC_H_MP3)
	$(XXD) -r -p -o 0 <(echo $(HEADER_FLAC)) $(FLAC_H_MP3)
	@# wav_header.mp3
	cp $(NOTAGS_MP3) $(WAV_H_MP3)
	$(XXD) -r -p -o 0 <(echo $(HEADER_WAV)) $(WAV_H_MP3)
	
	@# flac_header.wav
	cp $(NOTAGS_WAV) $(FLAC_H_WAV)
	$(XXD) -r -p -o 0 <(echo $(HEADER_FLAC)) $(FLAC_H_WAV)
	@# mp3v1_header.wav
	cp $(NOTAGS_WAV) $(MP31_H_WAV)
	$(XXD) -r -p -o 0 <(echo $(HEADER_MP31)) $(MP31_H_WAV)
	@# mp3v2_header.wav
	cp $(NOTAGS_WAV) $(MP32_H_WAV)
	$(XXD) -r -p -o 0 <(echo $(HEADER_MP32)) $(MP32_H_WAV)

recursiv: id3v2
	mkdir $(REC_DIR)
	mkdir -p $(REC_DIR_AX)
	
	@# copy to abc dir
	cp $(ID3V2_MP3) $(REC_DIR_A)/a.mp3
	cp $(ID3V2_MP3) $(REC_DIR_A)/b.mp3
	cp $(ID3V2_MP3) $(REC_DIR_A)/c.mp3

	@# copy to xyz dir
	cp $(ID3V2_MP3) $(REC_DIR_AX)/x.mp3
	cp $(ID3V2_MP3) $(REC_DIR_AX)/y.mp3
	cp $(ID3V2_MP3) $(REC_DIR_AX)/z.mp3

.PHONY: \
	all \
	clean \
	empty \
	notags \
	id3v1 \
	id3v2 \
	vorbis \
	symlink \
	perm \
	ext \
	recursiv \
	corrupt
