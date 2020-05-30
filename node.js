(async () => {
    const captureWebsite = require('capture-website');
    await captureWebsite.file('http://free.timeanddate.com/clock/i7b2ng0z/n122/tlmy/fcf00/ftb/bac0f0/pd2/tt0/tw1/tm1/th2/ta1/tb4', 'suplovanie.png');})();
    const suplovanie = new Attachment("./suplovanie.png");
    msg.channel.send(suplovanie);
})();
