Title:  Reimbursement for Exit Operators 
Author: Moritz 
Date: 2013-09-17

In July last year, Roger announced that BBG was interested in funding
fast exits. [[1]](https://lists.torproject.org/pipermail/tor-relays/2012-July/001433.html) The initial discussion on the mailing list continued
into August. If you're interested, you should consult the archive for
the various points raised. Since then, we've been discussing that topic
on and off. It matched with my plans to turn torservers.net into a
platform for many organizations, instead of just one single entity that
runs too many exit relays, so I agreed to take the lead. I posted a
status report of some sort on this list in April this year. [[2]](https://lists.torproject.org/pipermail/tor-relays/2013-April/001996.html)

The Wau Holland Foundation agreed to be one of the organizations willing
to handle the money and pass it on to other entities, be it single
operators or organizations. Both Torproject and Wau Holland Foundation
checked with their lawyers to see if this turns into a problem about
liability, and it looks like it does not. We're open for more
organizations to join in to manage the reimbursement process, but this
is what we've got for now.

In parallel, we've seen a growing number of organizations that were
created to turn donations into exit bandwidth. [[3]](http://www.torservers.net/partners.html)

Two issues with reimbursements, that were also mentioned in Roger's
initial posting, are that (1) you don't want to drive away all the
volunteers, and (2) you don't want to become dependent on (a single or a
handful of) sponsors. These are difficult issues, and I want to strongly
encourage everyone to keep contributing to the network. We really need
you, and we need more of you!

The second issue, dependence on funders, is on the one hand a harder
one, but on the other hand (in my opinion) a less relevant one. If
structures die and nodes have to be shut down because a funder backs
off, so be it. We hopefully don't change the picture too much in
comparison to the "unfunded times of today". The reimbursement process
does not guarantee a money stream, and the amounts are set on a
month-to-month basis, to encourage recipients to plan only short-term,
and only make contracts based on the money they have, disregarding what
they may or may not receive in the future. The current "bucket" is the
one-time BBG money, and it currently does not look like they will
restock it.

It might sound scary, but to satisfy the tax authorities (and to show
that it is a [hopefully] fair and transparent process), the Wau Holland
Foundation needs to have partners sign a contract. The contract does not
limit the partners abilities or restrict what they do, it only defines
the reimbursement process.

The way we want to start doing it now is not set in stone, and hopefully
now that we finally start handing out money it will encourage further
discussion around it. We want to refine the process over time, but it
looks like we just have to try with what we have now and learn from our
mistakes. Please don't be too hard with your criticism or you will
emotionally hurt me. I'm all ears. :-)

We want to reimburse based on the throughput per exit relay and
organization. To strengthen network diversity, we came up with the plan
to also factor in the location of the relays. There is a maximum amount
any entity can receive so we hopefully don't grow big monsters.

The contract [[4]](https://www.wauland.de/files/2013-07-19_TorExit_en.ott) specifies that there is a monthly amount, currently set
to $3500, split amongst all recipients (whom I started calling
"torservers partners"). The recipient share is calculated from the
throughput per relay * country factor, and the maximum amount per month
per partner is 500 Euro. The Wau Holland Foundation can currently only
reimburse via wire transfer.

The country factors can change over time, and are currently derived from
the total exit probability of that country. We can and should refine
this. Changes of these factors do not require new contracts.

Note that since the total amount of $3500 will be handed out every
month, as long as we have less than 6 entities signing the contract,
each entity will receive their maximum share of 500 Euro. I don't really
like the idea of a fixed monthly total handed out like that, but that's
what the lawyers and tax authorities signed off for Wau Holland
Foundation. It seems to be costly to re-evaluate such contracts, so this
is what we will stick to for now via WHF.

Technically, the monthly shares and the country factors are calculated
using a tool written by Lunar^^ (big thanks!). [[5]](https://people.torproject.org/~lunar/exit-funding.git) You can find an
example report at [[6]](https://www.torservers.net/misc/reimburse-output-2013-07.txt) (not the correct numbers, but you'll get the
idea). This monthly report will be sent to all partners, and once they
signed the contract they will simply get their monthly share.

As stated at the top, we want to start reimbursing this month. Please
let me know if you have any questions. We have a mailing list that is
public and read-only where we send important announcements, and require
every participant to be on and actually read. We have another mailing
list that is also read-only for the public, but people of the
participating organizations can post and discuss everything around
Torservers.net and reimbursements. [[7]](https://lists.torproject.org/pipermail/tor-relays/2013-May/002138.html)

The process to become a "partner" for now requires that I "know you".
So, if you're interested in becoming a partner, start social interaction
with me. I see that as a bad bottleneck, and I hope we can somehow get
rid of it in the future. I generally prefer "organizations" over single
persons, because (1) in most countries it seems to be really inexpensive
and easy to set up organizations and (2) the process of setting up such
entities includes that you gather enough people around you, so chances
are you will continue even if one of you drops out.

If you want to discuss, I prefer the tor-relays mailing list and our IRC
channel, #torservers on irc.oftc.net. I also explicitly want to invite
every partner to join that channel.
