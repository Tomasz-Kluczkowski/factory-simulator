import {Component, OnInit} from '@angular/core';
import {FactoryConfigAPIResource} from "../../models/factory-config.models";
import {FactoryConfigService} from "../../services/factory-config/factory-config.service";

@Component({
  selector: 'app-simulation',
  templateUrl: './simulation.component.html',
  styleUrls: ['./simulation.component.scss']
})
export class SimulationComponent implements OnInit {
  factoryConfigs: FactoryConfigAPIResource[];

  constructor(private factoryConfigService: FactoryConfigService) {
  }

  ngOnInit(): void {
    this.factoryConfigService.list().subscribe(
      (data) => {
        this.factoryConfigs = data;
      }
    );
  }
}
