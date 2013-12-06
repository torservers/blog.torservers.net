Title:  USB Sticks for Tails 
Author: Moritz 
Date: 2013-11-15

Ideally, you use TAILS from a read-only medium. CD is best, but many
devices these days don't have an optical drive, and handling CDs is not
as convenient as a USB stick.

For quite some time, people kept recommending the [TrekStor CS USB stick
](https://geizhals.de/trekstor-cs-8gb-50324-a240853.html), one of the
few sticks available in Germany with write-protection switch. Turns out
they use a new firmware, and now don't support booting from it in
read-only mode. The company confirmed this via email.

There are roughly no alternatives, and I figured I'm not the only one
looking for USB sticks with write protection switch. Via alibaba.com, a
"wholesale Chinese ebay", I contacted various Chinese suppliers, and
ended up ordering two samples. Even there, the selection of sticks with
write protection is very limited.

I ended up paying paying 60€ for the 2 samples because of shipping and
Western Union fees.

The sticks are not very fast, but acceptable, and boot in read-only
mode. They are not as slim as I hoped for, but the supplier is friendly,
production and shipping was very fast. (less than 2 weeks altogether).

Logo printing is cheap ($0.15 per stick), so to try the quality I also
had them print a logo on the samples.

I am still undecided whether I want the final sticks to have a logo, or
simply be blank to not attract too much attention. If you have a nice
idea for a logo, let me know. I want to order 100 sticks in time for
Chaos Communication Congress 30C3. The production cost is $4 per stick
(8GB), the final price (taxes, GEMA, shipping) will likely be around $15.

Pictures: <http://share.pho.to/48Egt>

## dmesg

     [55679.884123] usb 2-1.2: new high-speed USB device number 5 using ehci_hcd
     [55680.051089] usb 2-1.2: New USB device found, idVendor=058f,
     idProduct=6387
     [55680.051092] usb 2-1.2: New USB device strings: Mfr=1, Product=2,
     SerialNumber=3
     [55680.051094] usb 2-1.2: Product: Mass Storage
     [55680.051095] usb 2-1.2: Manufacturer: Generic
     [55680.051096] usb 2-1.2: SerialNumber: B6BA8F3F
     [55680.051459] scsi9 : usb-storage 2-1.2:1.0
     [55681.051827] scsi 9:0:0:0: Direct-Access     Generic  Flash Disk
      8.07 PQ: 0 ANSI: 4
      [55681.053860] sd 9:0:0:0: Attached scsi generic sg1 type 0
      [55681.055544] sd 9:0:0:0: [sdb] 15937536 512-byte logical blocks: (8.16
      GB/7.59 GiB)
      [55681.056665] sd 9:0:0:0: [sdb] Write Protect is off
      [55681.056676] sd 9:0:0:0: [sdb] Mode Sense: 23 00 00 00
      [55681.057742] sd 9:0:0:0: [sdb] Write cache: disabled, read cache:
      enabled, doesn't support DPO or FUA
      [55681.176618]  sdb: sdb1
      [55681.179808] sd 9:0:0:0: [sdb] Attached SCSI removable disk

## hdparm -t /dev/sdb

     /dev/sdb:
      Timing buffered disk reads:  54 MB in  3.07 seconds =  17.60 MB/sec

## dd if=tails-i386-0.21.iso of=/dev/sdb bs=1M

     891+1 records in
     891+1 records out
     934471680 bytes (934 MB) copied, 170.058 s, 5.5 MB/s
