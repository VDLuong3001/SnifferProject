import './style.css'

document.querySelector('#app').innerHTML = `
<h1>Network Packet Sniffer</h1>

<table border="1" width="100%">
<thead>
<tr>
<th>Source IP</th>
<th>Destination IP</th>
<th>Protocol</th>
</tr>
</thead>

<tbody id="packetTable"></tbody>

</table>
`

async function loadPackets(){

  try{

    const res = await fetch("http://localhost:5000/packets")
    const packets = await res.json()

    const table = document.getElementById("packetTable")

    table.innerHTML = ""

    packets.forEach(p => {

      const row = `
      <tr>
        <td>${p.src_ip}</td>
        <td>${p.dst_ip}</td>
        <td>${p.protocol}</td>
      </tr>
      `

      table.innerHTML += row

    })

  }catch(err){
    console.error("Error fetching packets:", err)
  }

}

setInterval(loadPackets, 2000)