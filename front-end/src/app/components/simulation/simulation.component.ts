import {Component, OnInit} from '@angular/core';
import {FactoryConfigAPIResource} from '../../models/factory-config.models';
import {SimulationAPIService} from '../../services/api/simulation/simulation-api.service';

@Component({
  selector: 'app-simulation',
  providers: [SimulationAPIService],
  templateUrl: './simulation.component.html',
  styleUrls: ['./simulation.component.scss']
})
export class SimulationComponent implements OnInit {
  factoryConfigs: FactoryConfigAPIResource[];

  constructor() {
  }

  ngOnInit(): void {}
}
