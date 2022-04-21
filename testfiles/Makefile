SOX			:= $(shell which sox)
LAME		:= $(shell which lame)
FLAC		:= $(shell which flac)
METAFLAC	:= $(shell which metaflac)
ID3V2		:= $(shell which id3v2)
ARTIST		:= "test artist"
ALBUM		:= "test album"
COMMENT		:= "test comment"
TITLE		:= "test title"
YEAR		:= $(shell date +%Y)

all: clean empty notags id3v1 id3v2 vorbis

clean:
	fd --type f --no-ignore flac$$\|mp3$$\|wav$$ -x rm {}
	fd --type d -x rm -r {}

empty:
	touch empty.flac
	touch empty.mp3
	touch empty.wav

notags:
	$(SOX) -c 2 -b 16 -n notags.wav synth 00:00.5 pinknoise
	$(FLAC) notags.wav
	$(LAME) -b 320 -h notags.wav

id3v1: notags
	cp notags.mp3 id3v1.mp3
	cp notags.wav id3v1.wav
	$(ID3V2) -1 -A $(ARTIST) -a $(ALBUM) -c $(COMMENT) -t $(TITLE) -y $(YEAR) -T 1/1 id3v1.mp3
	$(ID3V2) -1 -A $(ARTIST) -a $(ALBUM) -c $(COMMENT) -t $(TITLE) -y $(YEAR) -T 1/1 id3v1.wav

id3v2: notags
	cp notags.mp3 id3v2.mp3
	cp notags.wav id3v2.wav
	$(ID3V2) -2 -A $(ARTIST) -a $(ALBUM) -c $(COMMENT) -t $(TITLE) -y $(YEAR) -T 1/1 id3v2.mp3
	$(ID3V2) -2 -A $(ARTIST) -a $(ALBUM) -c $(COMMENT) -t $(TITLE) -y $(YEAR) -T 1/1 id3v2.wav

vorbis: notags
	cp notags.flac vorbis.flac
	$(METAFLAC) \
		--set-tag=ARTIST=$(ARTIST) \
		--set-tag=ALBUM=$(ALBUM) \
		--set-tag=COMMENT=$(COMMENT) \
		--set-tag=TITLE=$(TITLE) \
		--set-tag=YEAR=$(YEAR) \
		--set-tag=TRACKNUMBER=1 \
		--set-tag=TOTALTRACKS=1 \
		vorbis.flac

.PHONY: \
	all \
	clean \
	empty \
	notags \
	id3v1 \
	id3v2 \
	vorbis
